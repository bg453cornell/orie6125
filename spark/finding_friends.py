import sys
from pyspark import SparkConf, SparkContext

# Helper function to explode a list of friends into pairings
def explode_friends(tuple):
  if tuple != '':
    friends = tuple[1].split(",")

    for friend1 in friends:
      for friend2 in friends:
        if friend1 != friend2:
          yield (int(friend1), int(friend2))

# Helper function to sort recommendations. Compare the counts
# in descending order, then the IDs in ascending order.
def compare_friends(f1, f2):
  result = f2[1] - f1[1]

  if result == 0:
    result = f1[0] - f2[0]

  return result

# Helper function to sort and truncate the recommendation list
def sort_friends(itr):
  result = []

  for friend in itr:
    result.append(friend)
    result.sort(compare_friends)
    result = result[:10]

  return result

# For each line of input, generate user pairs that have common friends
# or are already friends
conf = SparkConf()
sc = SparkContext(conf=conf)

# Load the data and drop bad records
data = sc.textFile(sys.argv[1]).filter(lambda e: "\t" in e)

# Parse the data into IDs and lists of friends.
# We cache the results because we use them twice and don't want to have
# to recompute them.
pairs = data.map(lambda line: line.split("\t")).map(
    lambda parts: (int(parts[0]), parts[1].strip())).cache()

# Get a list of all direct friendships.
direct = pairs.flatMapValues(lambda friends: [int(f) for f in friends.split(",") if friends != ''])

# Get a list of all indirect friendships
indirect = pairs.flatMap(explode_friends)

# Remove the direct friendships from the indirect
indirect = indirect.subtract(direct)

# Now do the counting, just like in word count
counts = indirect.map(lambda (k, v): ((k, v), 1)).reduceByKey(lambda v1, v2: v1 + v2)

# Change the key to the user and group by user
counts = counts.map(lambda ((u, f), n): (u, (f, n))).groupByKey()

# Now sort the values by descending count and ascending ID and cap at 10.
# We use a helper function to do the sorting on the Spark side. Because of
# the groupByKey() operation, the values are ResultIterable objects, not lists,
# so we can't just call sort() on them. We could have instead done the
# sort and truncate after collecting the results, but it's better to let
# Spark do all the heavy lifting.
rec = counts.mapValues(lambda v: sort_friends(v))

# Only print the ones we want
wanted = [924, 8941, 8942, 9019, 9020, 9021, 9022, 9990, 9992, 9993]

for f in rec.filter(lambda (u, l): u in wanted).sortByKey().collect():
  print "%d\t%s" % (f[0], ",".join([str(r[0]) for r in f[1]]))

sc.stop()
