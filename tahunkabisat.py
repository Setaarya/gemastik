def is_leap_year(year):
    """Mengembalikan True jika year adalah tahun kabisat, jika tidak False."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def count_leap_years(start_year, end_year):
    """Menghitung jumlah tahun kabisat antara start_year dan end_year (inklusif)."""
    count = 0
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            count += 1
    return count

def main():
    print("Program untuk menghitung jumlah tahun kabisat")
    
    try:
        start_year = int(input("Masukkan tahun awal: "))
        end_year = int(input("Masukkan tahun akhir: "))
        
        if start_year > end_year:
            print("Tahun awal harus lebih kecil atau sama dengan tahun akhir.")
        else:
            leap_years_count = count_leap_years(start_year, end_year)
            print(f"Jumlah tahun kabisat antara {start_year} dan {end_year} adalah {leap_years_count}.")
    except ValueError:
        print("Tolong masukkan angka yang valid.")

if __name__ == "__main__":
    main()
