from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWriter import TextFileReaderWriter

#Test the default class
df = FileReaderWriter()
df.read()
df.write()

#Test the polymorphed methods
c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath = "sample2.csv", data = ["Hello", "World"])

j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data = ['foo', {'bar' : ('baz', None, 1.0, 2)}], filepath = "sample2.json")


txtf = TextFileReaderWriter()
txtf.read("TextFileReaderWriter.txt")
txtf.write(filepath = "TextFileReaderWriter(2).txt", data = ("This is the second sample for TextFileReaderWriter"))

