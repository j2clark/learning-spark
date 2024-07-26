from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("CustomerOrders")
sc = SparkContext(conf=conf)


def split_line(line):
    fields = line.split(",")
    customer_id = int(fields[0])
    amount = float(fields[2])
    return (customer_id, amount)


lines = sc.textFile("file:///C:/Users/j2cla/git/learning-spark/udemy/taming-big-data/customer-orders.csv")
orders = lines.map(split_line)
customerOrders = orders.reduceByKey(lambda x, y: x + y)
sortedBySpend = customerOrders.sortBy(lambda x: x[1], ascending=False)
# print(sorted.collect())

# print(spendByCustomer.collect())
for customer in sortedBySpend.collect():
    print(f'{customer[0]:02}: spend {customer[1]:.2f}')
    # print(str(customer[0]) + ": {:.2f}".format(customer[1]))
