place_data = {
    "place_id": 101,
    "name": "Eiffel Tower",
    "type": "Landmark",
    "description": "An iconic wrought-iron lattice tower on the Champ de Mars in Paris, France.",
    "city": "Paris",
    "country": "France",
    "avg_rating": 4.8,
    "num_reviews": 120000,
    "tags": "iconic, historical, viewpoint, romantic",
    "best_time_to_visit": "Spring or Fall"
}

print(type(place_data))
print(f"The {place_data['name']} is a famous {place_data['type']} known for {place_data['description'].lower().split('.')[0]}\n")

text_to_embed = (
    f"Place Name: {place_data['name']}. "
    f"Type: {place_data['type']}. "
    f"Description: {place_data['description']}. "
    f"Located in {place_data['city']}, {place_data['country']}. "
    f"Average Rating: {place_data['avg_rating']} out of 5 from {place_data['num_reviews']} reviews. "
    f"Tags: {place_data['tags']}. "
    f"Best time to visit: {place_data['best_time_to_visit']}."
)


# Using the same place_data example
text_to_embed = (
    f"Name: {place_data['name']}\n"
    f"Type: {place_data['type']}\n"
    f"Description: {place_data['description']}\n"
    f"Location: {place_data['city']}, {place_data['country']}\n"
    f"Rating: {place_data['avg_rating']} ({place_data['num_reviews']} reviews)\n"
    f"Keywords: {place_data['tags']}\n"
    f"Visit Season: {place_data['best_time_to_visit']}\n"
    # You can add more structured data, or even descriptive sentences
    f"The {place_data['name']} is a famous {place_data['type']} known for {place_data['description'].lower().split('.')[0]}."
)

print(type(text_to_embed))
print(text_to_embed)