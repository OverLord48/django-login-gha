from fastapi import FastAPI, Form
from config_db import conn


app = FastAPI()

@app.post("/logout")
async def logout(token: str = Form()):
    try:
        cur = conn.cursor()
        cur.execute(f"""
            DELETE FROM authtoken_token where key='{token}';""")
        conn.commit()
        cur.close()
        return {"OK":200}
    except Exception as e:
        print(f"Error {e}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=6000)
