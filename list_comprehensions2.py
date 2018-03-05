movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day", "Close Encounters of the Third Kind"]
#List of tuples of movie and release date
moviedates = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946), ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954), ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 1993), ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001),
    ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]
# gmovies = []
# for title in movies:
#     if title.startswith("G"):
#         gmovies.append(title)
#
# print(gmovies)

gmovies = [str.upper(title) for title in movies if title.startswith("G")]
print(gmovies)

pre2k = [title for (title, year) in moviedates if year < 2000]
print(pre2k)
