import pandas as pd

# DATABASE OLUŞTURMA...

df = pd.read_excel("movie_data.xlsx")  # Verilerimizin olduğu exceli okuyoruz..
filter_df = df.drop(columns=['MovieYear', 'MovieRate'])  # Kolay çalışmak için filtreleme yapıyoruz..
filter_df = filter_df[:100]

# KULLANICIYA SEÇİM YAPTIRTMA...

random_movie = filter_df["MovieName"].sample(10)  # MovieName sütunundan 10 tane rastgele item alıyoruz..

movie_list = []  # İtemlerin yazılacağı listeyi açıyoruz..
for i in random_movie:  # İtemleri listede topluyoruz..
    movie_list.append(i)

input_list = []  # Kullanıcı girdilerinin alınacağı listeyi açıyoruz..

counter = 0  # Sayacı 0'a eşitliyoruz..
while counter < 5:  # 5 adet film seçtirteceğimiz için sayacı 5 e kadar saydırtacağız..

    sheet_number = 1  # Vereceğimiz film listesini numaralandırmak için bir değişken açıyoruz ve 1 e eşitliyoruz..
    for x in movie_list:  # Topladığımız itemleri konsolda kullanıcıya yazdırıyoruz..
        print("{} - {}".format(sheet_number, x))
        sheet_number += 1

    print("Listeyi yenilemek icin '0' tusuna basiniz")  # Listeyi yenilemek için rehber cümle yazıyoruz..

    movie_input = int(input("Lutfen begendiginiz 5 filmin numarasini giriniz.."))  # Kullanıcı girdisini alıyoruz..

    if movie_input == 0:  # Eğer kullanıcı listeyi yenilemek isterse 0 a basıyor..

        random_movie = filter_df["MovieName"].sample(10)  # MovieName den yenı 10 tane rastgele item seçiyoruz..

        movie_list = []  # Film listesi oluşturma adımını tekrarlıyoruz..
        for i in random_movie:
            movie_list.append(i)
        input_list = []  # Girilen 0 ı silmek için girdi listesini sıfırlıyoruz..
    else:  # Eğer kullanıcı yenilemek istemezse  girdi almaya devam ediyoruz..

        input_list.append(movie_list[movie_input-1])  # Topladığımız girdilerin lıstedeki index numaralarına göre
        # listemizdeki isimlerle eşleştirip yeni listemize alıyoruz..
        del movie_list[movie_input-1]  # Seçilen filmi listeden siliyoruz..
        counter += 1  # Loopu devam ettiriyoruz..

print(input_list)  # Seçilen filmleri görüntülüyoruz..

# SEÇİLEN FİLMLERİN KATEGORİLERİNE AYRILMASI VE KATSAYI HESAPLANMASI...

genre_dict = {  # Seçilen filmleri kategorilerine ayırmak için tüm kategorileri içeren bir dictionary açıyoruz..
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

a = 0  # Sayacı 0 dan başlatıyoruz..
while a < len(input_list):  # Sayacı listemizdeki item sayısına kadar saydırtacağız..

    located_row = filter_df.loc[filter_df['MovieName'] == input_list[a]]  # input_list listesindeki film isimlerini kullanarak
    # database'deki satırlarına ulaşıyoruz ve bu satırları yeni bir değişkene atıyoruz..

    filter_df = filter_df[filter_df.MovieName != input_list[a]]  # Seçilen satırları databaseden çıkartıyoruz..

    list_row = []  # Satırları tutması için yeni bir liste açıyoruz..
    for l in located_row:
        list_row.append(located_row[l])  # Satırları yeni listemize atıyoruz..

    print(list_row[1])  # Satırımızda bulunan kategoriler sütununu MovieGenre görüntülüyoruz..

    for i in genre_dict:  # 'Drama''Crime' vs. dictionary'mizdeki stringleri tek tek geziyoruz..
        if str(list_row[1]).__contains__(i):  # Satırdaki MovieGenre sütunu dictionary mizden aldığımız kategoriyle eşleiyorsa
            genre_dict[i] += 1  # bu kategorinin değerini 1 arttırıyoruz..

    a += 1  # Sonra loop'u devam ettiriyoruz..


for x, y in genre_dict.items(): # Dictionary'yi konsolda görüntülüyoruz..
    print(x, y)

#  DATABASE PUANLAMASI...

filter_df['PointTotal'] = 0  # Filmlerimizin puanlarının toplanması için database'e yeni bir sütın ekliyoruz ve değerleri sıfıra eşitliyoruz..
for genre in genre_dict:  # Dictionary'mizdeki kategorileri tek tek geziyoruz..
    col_lock = filter_df[genre]  # Kategorinin bulunduğu sütuna tutunuyoruz..
    col_lock = col_lock * genre_dict[genre]  # Kategori sütununu dictionary'mizdeki katsayıyla çarpıyoruz..
    filter_df['PointTotal'] += col_lock  # Yeni değerlerle oluşan sütunu PointTotal sütununa ekliyoruz..

# TAVSİYE YAPILMASI...

recommender = filter_df.sort_values(by='PointTotal',ascending=False)  # Database'i PointTotal sütununa göre azalan sıraya göre sıralıyoruz..
print(recommender.head(25))  # Sonuçları kullanıcıya gösteriyoruz..





