from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to invent it. - Alan Kay",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "If you can dream it, you can do it. - Walt Disney",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Never bend your head. Always hold it high. Look the world straight in the eye. - Helen Keller",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "It is always the simple that produces the marvelous. - Amelia Barr",
    "The world is full of magical things patiently waiting for our wits to grow sharper. - Bertrand Russell",
    "Let us make our future now, and let us make our dreams tomorrow's reality. - Malala Yousafzai",
    "All you need is the plan, the road map, and the courage to press on to your destination. - Earl Nightingale",
    "The glow of one warm thought is to me worth more than money. - Thomas Jefferson",
    "Once you choose hope, anything’s possible. - Christopher Reeve",
    "Try to be a rainbow in someone else's cloud. - Maya Angelou",
    "You do not find the happy life. You make it. - Camilla E. Kimball",
    "The most wasted of days is one without laughter. - E.E. Cummings",
    "You must do the things you think you cannot do. - Eleanor Roosevelt",
    "It isn't where you came from. It's where you're going that counts. - Ella Fitzgerald",
    "It is never too late to be what you might have been. - George Eliot",
    "You make a life out of what you have, not what you're missing. - Kate Morton",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "Life is not about finding yourself. Life is about creating yourself. - George Bernard Shaw",
    "If opportunity doesn't knock, build a door. - Milton Berle",
    "Setting goals is the first step in turning the invisible into the visible. - Tony Robbins",
    "Your passion is waiting for your courage to catch up. - Isabelle Lafleche",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "You are enough just as you are. - Meghan Markle",
    "You have to be at your strongest when you’re feeling at your weakest. - Unknown",
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
    "Great minds discuss ideas; average minds discuss events; small minds discuss people. - Eleanor Roosevelt",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it’s done. - Nelson Mandela"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify(quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
