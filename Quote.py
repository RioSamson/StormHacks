import random

class Quote:

    def getQuote(self):
        quotes = ["“When life gives you lemons, squirt someone in the eye.”– Cathy Guisewite"
                    , "“Be happy – it drives people crazy.”– Unknown"
                    , "“Optimist: someone who figures that taking a step backward after taking a step forward is not a disaster; it's more like a cha-cha.”– Robert Brault"
                    , "“Live each day like it's your second to the last. That way you can fall asleep at night.”– Jason Love"
                    , "“Even a stopped clock is right twice every day. After some years, it can boast of a long series of successes.”– Marie Con Ebner-Eschenbach"
                    , "“People who wonder whether the glass is half empty or half full miss the point. The glass is refillable.” – Simon Sinek"
                    , "“Learn from the mistakes of others. You can never live long enough to make them all yourself.” – Groucho Marx"
                    , "“Luck is what you have left over after you give 100 percent.” – Langston Coleman"
                    , "“When you do not know what you are doing and what you are doing is the best – that is inspiration.” – Robert Bresson"
                    , "“Consider the postage stamp: its usefulness consists in the ability to stick to one thing ’til it gets there.” – Josh Billings"
                    , "“Bad decisions make good stories.” – Ellis Vidler"
                    , "“Think like a proton. Always positive.” – Author Unknown"
                    , "“Opportunity is missed by most people because it is dressed in overalls and looks like work.” – Thomas Edison"
                    , "“I always wanted to be somebody, but now I realize I should have been more specific.” – Lily Tomlin"
                    , "“If you’re going to be able to look back on something and laugh about it, you might as well laugh about it now.” – Marie Osmond"
                    , "“Here is a test to find whether your mission on earth is finished: If you’re alive it isn’t.” – Richard Bach"
                    , "“When I hear somebody sigh, ‘Life is hard’, I am always tempted to ask, ‘Compared to what?’” – Sydney Harris"
                    , "“There is nothing in a caterpillar that tells you it's going to be a butterfly.”– Buckminster Fuller"
                    , "“Life itself is the most wonderful fairy tale.”– Hans Christian Andersen"
                    , "“If you have good thoughts they will shine out of your face like sunbeams and you will always look lovely.” – Roald Dahl"
                    , "“You’ve got to do your own growing, no matter how tall your grandfather was.” – Irish Proverb"
                    , "“When you know better, you do better.” – Maya Angelou"
                    , "“You’re braver than you believe, and stronger than you seem, and smarter than you think.” – A. A. Milne/Christopher Robin"
                    , "“You have brains in your head, you have feet in your shoes. You can steer yourself any direction you choose. You’re on your own. And you know what you know. And YOU are the one who’ll decide where to go.” – Dr. Seuss"
                    , "“If they don’t like you for being yourself, be yourself even more.” – Taylor Swift"
                    , "“No one is perfect — that’s why pencils have erasers.” – Anonymous"
                    , "“I need to listen well so that I hear what is not said.” – Thuli Madonsela"
                    , "“We grow great by dreams.” – Woodrow Wilson"
                    , "“We do not need magic to change the world, we carry all the power we need inside ourselves already. We have the power to imagine better.” – J. K. Rowling"
                    , "“Why fit in when you were born to stand out?” – Dr. Seus"
                    , "“Believe that life is worth living and your belief will help create the fact.”– William James"
                    , "“Choose to be optimistic, it feels better.” – Dalai Lama"
                    , "“Even if happiness forgets you a little bit, never completely forget about it.”– Jacques Prevert"
                    , "“In three words I can sum up everything I’ve learned about life. It goes on.”– Robert Frost"
                    , "“It doesn’t matter how slow you go, as long as you don’t stop.”– Confucius"
                    , "“Success is the sum of small efforts, repeated day-in and day-out.”– Robert Collier"
                    , "“The meaning of life is to find your gift. The purpose of life is to give it away.”– Anonymous"
                    , "“You are today where your thoughts have brought you; you will be tomorrow where your thoughts take you.”– James Allen"
                    , "“You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.”– George Lorimer"
                    , "“Believe that life is worth living, and your belief will help create the fact.”– William James"
                    , "“Choose to be optimistic; it feels better.” – Dalai Lama"
                    , "“Even if happiness forgets you a little bit, never completely forget about it.”– Jacques Prevert"
                    , "“In three words, I can sum up everything I’ve learned about life. It goes on.”– Robert Frost"
                    , "“It doesn’t matter how slow you go, as long as you don’t stop.”– Confucius"
                    , "“Success is the sum of small efforts, repeated day in and day-out.”– Robert Collier"
                    , "“The meaning of life is to find your gift. The purpose of life is to give it away.”– Anonymous"
                    , "“You are today where your thoughts have brought you; you will be tomorrow where your thoughts take you.”– James Allen"
                    , "“You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.”– George Lorimer"
                    , "“Your problem isn’t the problem. Your reaction is the problem.”– Anonymous"
                    , "“Three things in life – your health, your mission, and the people you love. That’s it.” – Naval Ravikant"
                    , "“Accept no one’s definition of your life; define yourself.” – Harvey Fierstein"
    ]
        index = random.randint(0, len(quotes))
        return quotes[index]
    