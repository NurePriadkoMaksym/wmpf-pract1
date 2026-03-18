import requests

name = input("Enter your name: ")
print(f"Hello, {name}!")

numbers = list(range(1, 21))
print("Числа та їх квадрати:")
for num in numbers:
    print(f"Число: {num}, Квадрат: {num**2}")

def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
even_nums = even_numbers(numbers)
print("Парні числа зі списку:", even_nums)

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print("API")
if response.status_code == 200:
    data = response.json()
    
    for post in data[:5]:
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
else:
    print("Помилка при отриманні даних:", response.status_code)
