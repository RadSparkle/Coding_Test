N = int(input())
pattern = "666"
movie_title = 666
cnt = 1

while cnt != N:
    movie_title+=1
    if pattern in str(movie_title):
        cnt +=1

print(movie_title)