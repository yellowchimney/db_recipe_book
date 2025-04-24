DROP TABLE IF EXISTS recipes;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255), 
    cooking_time INT, 
    rating INT);

INSERT INTO recipes (name, cooking_time, rating) 
VALUES  ('Spaghetti Carbonara', 25, 5),
        ('Chicken Tikka Masala', 45, 4),
        ('Beef Stroganoff', 40, 4),
        ('Miso Ramen', 50, 5),
        ('Shakshuka', 30, 4),
        ('Butternut Squash Soup', 35, 5),
        ('Pad Thai', 40, 4),
        ('Margherita Pizza', 20, 5),
        ('Falafel Wrap', 25, 4),
        ('Fish Tacos', 30, 4),
        ('Lasagna', 60, 5),
        ('Vegetable Stir Fry', 20, 3),
        ('Butter Chicken', 45, 5),
        ('Eggplant Parmesan', 50, 4),
        ('Chili con Carne', 55, 5);

