import praw
import sqlite3


def reddit_shit():
    reddit = praw.Reddit(
        client_id="mgL2amGhWYc2jg",
        client_secret="GFuozwhWZiy7eNNlsBSWUS74SfU",
        user_agent="Mozilla:Windows:0.1.0",
        username="BiTz_and_Bobs",
        password="clover5002"
    )

    #this is to find the description... gonna use this bad boy later
    #desciption = reddit.subreddit("learningpython").description
    #print(desciption)

    return reddit



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn

def select_task_priority(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM subreddits")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def subscribers(conn, reddit):
    
    cur = conn.cursor()
    cur.execute("SELECT name FROM subreddits")

    rows = cur.fetchall()

    sql = 'DELETE FROM subreddits WHERE name=?'

    for row in rows:
        sub = row[0]
        print(sub)
        try:
            k = reddit.subreddit(sub)
            sub_num = k.subscribers
        except:
            cur.execute(sql, (sub,))
            conn.commit()
            print(sub + "was deleted")
            continue

        if(sub_num < 2000):
            cur.execute(sql, (sub,))
            conn.commit()


if __name__ == "__main__":
    reddit = reddit_shit()
    db_file = "subreddits.db"
    conn = create_connection(db_file)
    #select_task_priority(conn)
    subscribers(conn, reddit)

    #if reddit.subreddit("name") = none then delete

    