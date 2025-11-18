import psycopg2

def log_chat(user_question, ai_response):

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO chat_log (user_question, ai_response)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (user_question, ai_response))
        conn.commit()
    finally:
        cursor.close()
        conn.close()