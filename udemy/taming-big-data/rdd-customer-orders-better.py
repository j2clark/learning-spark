from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("CustomerOrders")
sc = SparkContext(conf=conf)


def split_line(line):
    fields = line.split(",")
    customer_id = int(fields[0])
    amount = float(fields[2])
    # number of orders
    # count = 1
    return (customer_id, (amount, 1))


lines = sc.textFile("file:///C:/Users/j2cla/git/learning-spark/udemy/taming-big-data/customer-orders.csv")
orders = lines.map(split_line)
customerOrders = orders.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
# print(customerOrders.collect())
sortedBySpend = customerOrders.sortBy(lambda x: x[1], ascending=False)
# print(sortedBySpend.collect())

for customer in sortedBySpend.collect():
    cid = customer[0]
    data = customer[1]
    spend = data[0]
    count = data[1]
    avg = spend / count
    print(f'{cid:02}: spend ${spend:.2f}, orders {count}, avg spend/order {avg:.2f}')