CREATE TABLE "food_intake" (
  "user_id" intiger,
  "calories" integer,
  "protein" integer,
  "carbs" integer,
  "fats" integer,
  "fiber" intiger,
  "day" timestamp
);

CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "username" varchar,
  "password" varchar,
  "weight" integer,
  "bodyfat" integer,
  "daily_calories" integer,
  "daily_protein" integer,
  "daily_carbs" integer,
  "daily_fats" integer,
  "daily_fiber" intiger
);

CREATE TABLE "standard_meals" (
  "user_id" integer PRIMARY KEY,
  "meal_name" varchar,
  "calories" integer,
  "protein" integer,
  "carbs" integer,
  "fats" integer,
  "fiber" intiger
);

ALTER TABLE "food_intake" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "standard_meals" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
