import os
import random
import datetime
from plyer import notification

# List of motivational quotes with descriptions
quotes = [
    ("The best way to predict the future is to create it.", "Creating your own future through proactive efforts."),
    ("You only live once, but if you do it right, once is enough.", "Live life to the fullest, making the most of every moment."),
    ("Success is not the key to happiness. Happiness is the key to success.", "Find happiness in what you do to achieve true success."),
    ("Believe you can and you're halfway there.", "Self-belief is crucial in achieving your goals."),
    ("Don't watch the clock; do what it does. Keep going.", "Keep moving forward regardless of time."),
    ("The only limit to our realization of tomorrow is our doubts of today.", "Overcome doubts to reach your potential."),
    ("The harder you work for something, the greater you'll feel when you achieve it.", "Hard work leads to rewarding achievements."),
    ("Dream bigger. Do bigger.", "Set higher goals and take larger actions."),
    ("Don’t stop when you’re tired. Stop when you’re done.", "Persist until you’ve completed your goals."),
    ("Wake up with determination. Go to bed with satisfaction.", "Start each day with motivation and end with a sense of achievement."),
    ("Do something today that your future self will thank you for.", "Act now to benefit your future self."),
    ("Little things make big days. Great days come from hard work and perseverance.", "Small efforts accumulate into significant achievements."),
    ("The key to success is to focus on goals, not obstacles.", "Keep your eyes on your goals rather than the challenges."),
    ("Dream it. Believe it. Build it.", "Visualize, believe, and work towards your dreams."),
    ("Motivation is what gets you started. Habit is what keeps you going.", "Sustained success comes from consistent habits."),
    ("You are never too old to set another goal or to dream a new dream.", "Age is not a barrier to setting new goals."),
    ("You don’t have to be great to start, but you have to start to be great.", "Beginning is essential to achieving greatness."),
    ("Everything you’ve ever wanted is on the other side of fear.", "Face your fears to obtain your desires."),
    ("Success doesn’t just find you. You have to go out and get it.", "Actively pursue success instead of waiting for it."),
    ("The only way to achieve the impossible is to believe it is possible.", "Belief in the possible leads to achieving the impossible."),
    ("Push yourself, because no one else is going to do it for you.", "Self-motivation is key to progress."),
    ("Great things never come from comfort zones.", "Step out of your comfort zone to achieve greatness."),
    ("Dream it. Wish it. Do it.", "Visualize and then act upon your dreams."),
    ("Success is not for the lazy.", "Achieving success requires effort and diligence."),
    ("The more you dream, the farther you get.", "Expanding your dreams can lead to greater achievements."),
    ("Work hard in silence, let success be your noise.", "Let your achievements speak for themselves."),
    ("Don’t wait for opportunity. Create it.", "Take initiative to create your own opportunities."),
    ("Dream it. Believe it. Chase it.", "Visualize, believe, and pursue your dreams."),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Perseverance through success and failure is crucial."),
    ("Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", "Self-belief helps overcome any challenge."),
    ("The only place where success comes before work is in the dictionary.", "Work precedes success."),
    ("Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.", "Let dreams guide you rather than fears."),
    ("Opportunities don't happen. You create them.", "Create your own opportunities."),
    ("Success usually comes to those who are too busy to be looking for it.", "Success often comes to those who are actively engaged."),
    ("Don’t be afraid to give up the good to go for the great.", "Be willing to leave behind good opportunities for great ones."),
    ("I find that the harder I work, the more luck I seem to have.", "Hard work often creates its own luck."),
    ("Success is walking from failure to failure with no loss of enthusiasm.", "Maintain enthusiasm despite setbacks."),
    ("The way to get started is to quit talking and begin doing.", "Action is the first step to success."),
    ("You miss 100% of the shots you don’t take.", "Taking risks is essential for success."),
    ("Hardships often prepare ordinary people for an extraordinary destiny.", "Challenges can lead to remarkable achievements."),
    # Add more quotes here...
]

# Function to get today's quote
def get_todays_quote():
    quote, description = random.choice(quotes)
    return quote, description

# Function to display the notification
def show_notification(quote, description):
    notification.notify(
        title="Motivational Quote",
        message=f"{quote}\n\n{description}",
        timeout=10  # Notification duration in seconds
    )

# Main function
def main():
    today = datetime.date.today()
    user_home_dir = os.path.expanduser('~')
    last_run_file = os.path.join(user_home_dir, "last_run.txt")

    if os.path.exists(last_run_file):
        with open(last_run_file, "r") as file:
            last_run_date = file.read().strip()

        if last_run_date == str(today):
            return  # No need to show notification if already shown today

    # Show notification
    quote, description = get_todays_quote()
    show_notification(quote, description)

    # Update the last run date
    with open(last_run_file, "w") as file:
        file.write(str(today))

if __name__ == "__main__":
    main()
