import pandas as pd

# مسیر فایل CSV
data_path = r"C:/Users/Asus/Desktop/MovieData/Dataset.csv"

# خواندن داده‌ها
df = pd.read_csv(data_path)

# محاسبه آمار کلیدی
rating_stats = df["rating"].agg(["mean", "min", "max"])
user_counts = df["user_id"].value_counts()
movie_counts = df["item_id"].value_counts()

# ساخت جدول نتایج
summary = pd.DataFrame({
    "عنوان": [
        "تعداد کل ریتینگ‌ها",
        "تعداد کاربران",
        "تعداد آیتم‌ها",
        "میانگین امتیاز",
        "حداقل امتیاز",
        "حداکثر امتیاز",
        "کاربر با بیشترین ریت",
        "تعداد ریت‌های آن کاربر",
        "آیتم با بیشترین ریت",
        "تعداد ریت آن آیتم",
    ],
    "مقدار": [
        len(df),
        df["user_id"].nunique(),
        df["item_id"].nunique(),
        round(rating_stats["mean"], 2),
        rating_stats["min"],
        rating_stats["max"],
        user_counts.idxmax(),
        user_counts.max(),
        movie_counts.idxmax(),
        movie_counts.max(),
    ]
})

# چاپ جدول و اطلاعات پایه
print(summary.to_string(index=False))
print("\nفایل با موفقیت خوانده شد ✔")
print("تعداد ردیف‌ها:", len(df))
print("ستون‌ها:", list(df.columns))
