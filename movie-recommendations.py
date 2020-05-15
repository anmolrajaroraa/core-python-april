import random

dataset = {
    "thriller": ["In The Tall Grass", "The Purge", "Thriller", "Inception", "Shutter Island"],
    "horror": ["IT", "Insidious", "Annabelle", "Conjuring", "Wrong Turn"],
    "sci-fi": ["Gravity", "Interstellar", "Star Wars", "Guardians of the Galaxy", "Godzilla"],
    "comedy": ["Chal Mera Putt", "Carry On Jatta", "Vadhaiyan Ji Vadhaiyan", "Daddy Cool Munde Fool", "Mel Krade Rabba"],
    "romantic": ["Jatt n Juliet", "Carry On Jatta", "Sufna", "Veer Zaara", "50 Shades Darker"]
}
user1 = ["Inception", "Insidious", "Annabelle", "Interstellar", "Star Wars",
         "Carry On Jatta", "Jatt n Juliet"]
user2 = ["Inception", "Shutter Island", "IT", "Insidious", "Annabelle", "Conjuring", "Wrong Turn", "Gravity", "Interstellar",
         "Star Wars", "Guardians of the Galaxy", "Godzilla", "Vadhaiyan Ji Vadhaiyan", "Daddy Cool Munde Fool", "Jatt n Juliet", "Sufna"]

keys = list(dataset.keys())

# create an empty dictionary using the categories from dataset
most_watched_genres_user1 = dict.fromkeys(keys, 0)
most_watched_genres_user2 = dict.fromkeys(keys, 0)

# check which movie belongs to which genre and increment that genre value in the dictionary we have just created above
for movie in user1:
    for genre in keys:
        if movie in dataset[genre]:
            print(movie, genre)
            most_watched_genres_user1[genre] += 1
for movie in user2:
    for genre in keys:
        if movie in dataset[genre]:
            print(movie, genre)
            most_watched_genres_user2[genre] += 1
print(most_watched_genres_user1)
print(most_watched_genres_user2)

# extract only the count of movies watched in each genre
most_watched_genres_user1 = list(most_watched_genres_user1.values())
most_watched_genres_user2 = list(most_watched_genres_user2.values())
print(most_watched_genres_user1)
print(most_watched_genres_user2)
fav_category_user1_count = max(most_watched_genres_user1)
fav_category_user2_count = max(most_watched_genres_user2)
print(fav_category_user1_count)
print(fav_category_user2_count)

# get the category of most watched movies
fav_category_user1_index = most_watched_genres_user1.index(
    fav_category_user1_count)
fav_category_user2_index = most_watched_genres_user2.index(
    fav_category_user2_count)
print(fav_category_user1_index)
print(fav_category_user2_index)
fav_category_user1 = keys[fav_category_user1_index]
fav_category_user2 = keys[fav_category_user2_index]
print(fav_category_user1)
print(fav_category_user2)

user1_watched_movies_in_fav_category_of_user1 = set()
user2_watched_movies_in_fav_category_of_user1 = set()

# find the movies watched by both users in fav category of user1
for movie in user1:
    if movie in dataset[fav_category_user1]:
        user1_watched_movies_in_fav_category_of_user1.add(movie)
for movie in user2:
    if movie in dataset[fav_category_user1]:
        user2_watched_movies_in_fav_category_of_user1.add(movie)

print(user1_watched_movies_in_fav_category_of_user1)
print(user2_watched_movies_in_fav_category_of_user1)

# find the movies that user1 has not watched in his/her fav category but user2 has watched them so we can use these movies for recommendation to user1 for what to watch next
to_be_recommended_movies = list(
    user2_watched_movies_in_fav_category_of_user1 - user1_watched_movies_in_fav_category_of_user1)

print(f"Recommended movie is {random.choice(to_be_recommended_movies)}")
