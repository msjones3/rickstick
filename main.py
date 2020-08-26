from flask import *
import requests
from random import randint

app = Flask(__name__)
# images of Ricks and Sticks - stored as lists
ricks = ['https://upload.wikimedia.org/wikipedia/en/a/a6/Rick_Sanchez.png',
        'https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg',
        'https://www.nme.com/wp-content/uploads/2016/09/2014RickAstley_Getty109255193201014-1-696x464.jpg',
        'data:image/jpeg;base64,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',
        'https://media2.s-nbcnews.com/j/newscms/2017_45/2219761/nixon-68_96b34ecbfb09bd4d03b5ba41c285e5a1.fit-760w.jpg',
        'https://media2.s-nbcnews.com/j/newscms/2020_29/3396653/200713-ricky-martin-jm-1503_ecb3be20ea2181766512a87fc2742bff.nbcnews-fp-1200-630.jpg']
sticks = ['https://www.toyhalloffame.org/sites/www.toyhalloffame.org/files/toys/square/stick_0.png',
        'https://www.kmart.com.au/wcsstore/Kmart/images/ncatalog/f/9/42630029-1-f.jpg',
        'https://media.istockphoto.com/photos/wooden-ice-cream-stick-isolated-on-white-background-clipping-path-picture-id687931678?k=6&m=687931678&s=612x612&w=0&h=ELfcPN7SixBaSm5udeex_qQb0MfXU8NGJIMKY1g47kM=',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQl02tDud_qmknq1K4nFtPePkniHDXOS8fwUw&usqp=CAU',
        'data:image/jpeg;base64,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',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTXsbp4RT0NK1quy2Pq2VoD2QFit871Z07-A&usqp=CAU']


# get a random number from 0 to the number passed into the function
def getRandom(num):
    return randint(0,num)

@app.route("/", methods=["GET", "POST"])
def main():
    # randomly choose rick or stick
    choice = getRandom(2)
    if choice == 1:
        return render_template('display.html', image=ricks[getRandom(5)])
    else:
        return render_template('display.html', image=sticks[getRandom(5)])

app.run(debug=True)
