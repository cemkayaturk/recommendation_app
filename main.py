import pandas as pd

df = pd.read_excel("movie_data.xlsx") # exceli oku
filter_df = df.drop(columns=['MovieYear', 'MovieRate']) # exceli filtrele
filter_df = filter_df[:100]

random_movie = filter_df["MovieName"].sample(10) # 10 tane rastgele item sec

movie_list = []                    # itemlerin yazilacagi list
for i in random_movie:             # itemleri liste topla
    movie_list.append(i)
input_list = []                    # girdi listesi
counter = 0
while counter < 5:                 # film secme loopu

    sheet_number = 1
    print("Listeyi yenilemek icin '0' tusuna basiniz")
    for x in movie_list:
        print("{} - {}".format(sheet_number, x))    #itemleri yaz
        sheet_number += 1
    movie_input = int(input("Lutfen begendiginiz 5 filmin numarasini giriniz.."))  #input gir
    if movie_input == 0:
        random_movie = filter_df["MovieName"].sample(10)  # 10 tane rastgele item sec

        movie_list = []  # itemlerin yazilacagi list
        for i in random_movie:  # itemleri liste topla
            movie_list.append(i)
        input_list = []  # girdi listesi
    else:

        input_list.append(movie_list[movie_input-1])    # inputlarin indexine bagli oldugu stringi liste topla
        del movie_list[movie_input-1]   # girilen inoutun indexini sil
        counter += 1

print(input_list)

a = 0  #while loopt arttirmak icin 0la baslayan degisken
genre_dict = {
        'Drama': 0,
        'Crime': 0,
        'Action': 0,
        'Sci-Fi': 0,
        'Romance': 0,
        'Fantasy': 0,
        'Adventure': 0,
        'Thriller': 0,
        'War': 0,
        'Western': 0,
        'History': 0,
        'Biography': 0,
        'Sport': 0,
        'Comedy': 0,
        'Musical': 0,
        'Music': 0,
        'Mystery': 0,
        'Family': 0,
        'Animation': 0,
        'Film-Noir': 0,
        'Documentary': 0,
        'Short': 0,
    }
while a < len(input_list):  # loopun input listesinin sonuna kadar donmesi icin

    located_row = filter_df.loc[filter_df['MovieName'] == input_list[a]]  # input listesindeki stringi kullanarak datamizin
    filter_df = filter_df[filter_df.MovieName != input_list[a]]
    # icindeki satira tutunup, satiri located_row degiskenine atiyoruz
    list_row = []  # satir objelerini tutmasi icin bos bir liste aciyoruz
    for l in located_row:
        list_row.append(located_row[l])  # satir objelerini bos listeye ekliyoruz

    print(list_row[1])

    for i in genre_dict:  # 'Drama''Crime' vs. dictionary mizdeki stringleri tek tek geziyoruz
        if str(list_row[1]).__contains__(
                i) == True:  # str(list_row[1]) ile listrowa attigimiz satir degiskeninin 1. indexine erisiyoruz || yani "MovieGenre" sutunundaki degeri aliyoruz ve stringe donusturuyoruz
            genre_dict[i] += 1  # .contains ile dictionarydeki stringler str(list_row[1]) un icinde varsa bu stringin bagli oldugu degeri 1 arttir diyoruz

    a += 1  # sonra loopu devam ettiriyoruz


for x,y in genre_dict.items(): # dictionary yi konsolda goruntulemek icin
  print(x,y)

filter_df['PointTotal'] = 0
for genre in genre_dict:
    col_lock = filter_df[genre]
    col_lock = col_lock * genre_dict[genre]
    filter_df['PointTotal'] += col_lock

recommender = filter_df.sort_values(by='PointTotal',ascending=False)
print(recommender.head(10))





