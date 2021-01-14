import uvicorn
import sys

def main():
    pass

if __name__ == "__main__":
    uvicorn.run(app="peppa:app",port="2222",host="127.0.0.1")
    sys.exit(int(main() or 0))