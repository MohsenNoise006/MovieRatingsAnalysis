import pandas as pd
import os

# مسیر دقیق فایل‌ها (بر اساس گفته شما)
initial_path = r"D:\Codpython\MovieData\Dataset.csv"
new_path     = r"D:\Codpython\MovieData\dataset1.csv"

# بررسی وجود فایل‌ها
def check_file(path):
    if not os.path.isfile(path):
        print(f"❌ فایل یافت نشد: {path}")
        exit()
    else:
        print(f"✔ فایل پیدا شد: {path}")

check_file(initial_path)
check_file(new_path)

# خواندن دیتاست‌ها
df_initial = pd.read_csv(initial_path)
df_new = pd.read_csv(new_path)

print("\n--- اطلاعات اولیه ---")
print(df_initial.head())
print("\n--- اطلاعات دیتاست جدید ---")
print(df_new.head())

# حذف سطرهای دارای NaN از دیتاست جدید

df_cleaned = df_new.dropna()
removed_rows = df_new[df_new.isna().any(axis=1)]

print("\n✔ تعداد سطرهای حذف شده:", len(removed_rows))

# پیدا کردن سطرهای حذف‌شده‌ای که در دیتاست اولیه وجود دارند

common_removed = pd.merge(
    removed_rows,
    df_initial,
    on=["user_id", "item_id", "rating"],  # ستون‌ها اصلاح شد
    how="inner"
)

print("✔ سطرهای حذف‌شده که در دیتاست اولیه هم بودند:", len(common_removed))

#  محاسبات آماری امتیازها

if "rating" in df_cleaned.columns:
    print("\n--- آمار امتیازها ---")
    print("تعداد کاربران:", df_cleaned["user_id"].nunique())
    print("تعداد فیلم‌ها:", df_cleaned["item_id"].nunique())
    print("تعداد ریتینگ‌ها:", df_cleaned["rating"].count())
    print("میانگین:", df_cleaned["rating"].mean())
    print("حداقل:", df_cleaned["rating"].min())
    print("حداکثر:", df_cleaned["rating"].max())

    # کاربری که بیشترین فیلم را رت کرده
    top_user = df_cleaned["user_id"].value_counts().idxmax()

    # فیلمی که بیشترین ریت را گرفته
    top_movie = df_cleaned["item_id"].value_counts().idxmax()

    print("\nبیشترین کاربر فعال:", top_user)
    print("پر امتیازترین فیلم:", top_movie)

# ذخیره خروجی‌ها

output_cleaned = r"D:\Codpython\MovieData\Dataset_Cleaned.csv"
output_removed = r"D:\Codpython\MovieData\Removed_Rows.csv"
output_common  = r"D:\Codpython\MovieData\Common_Removed.csv"

df_cleaned.to_csv(output_cleaned, index=False)
removed_rows.to_csv(output_removed, index=False)
common_removed.to_csv(output_common, index=False)

print("\n✔ فایل‌ها با موفقیت ذخیره شدند:")
print(output_cleaned)
print(output_removed)
print(output_common)

