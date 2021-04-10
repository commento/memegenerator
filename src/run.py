
from QuoteEngine import Ingestor
from MemeEngine import MemeGenerator



print(Ingestor.parse('./_data/SimpleLines/SimpleLines.docx'))
print(Ingestor.parse('./_data/SimpleLines/SimpleLines.csv'))
print(Ingestor.parse('./_data/SimpleLines/SimpleLines.pdf'))
print(Ingestor.parse('./_data/SimpleLines/SimpleLines.txt'))





mg = MemeGenerator("tmp")
print(mg.make_meme('_data/photos/dog/xander_2.jpg',
                        'woof!',
                        'Mamma',
                        width=500))