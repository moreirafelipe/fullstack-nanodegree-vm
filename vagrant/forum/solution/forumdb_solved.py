import psycopg2

user = 'app'
password = 'appaccess'
host = '34.95.251.220'
database = 'postgres'


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        database=database)

    c = db.cursor()
    c.execute("select content, time from posts order by time desc")
    db.close()
    return c.fetchall()


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""

    db = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    c = db.cursor()
    c.execute("insert into posts values('%s')" % content)
    db.commit()
