from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('Local').setAppName('My first app')
sc = SparkContext(conf=conf)
