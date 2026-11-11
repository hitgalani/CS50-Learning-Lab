# PAPER A - LIBRARY DATA

# Step 1: Create Library Data
library_data <- data.frame(
  BookID = c(1, 2, 3, 4, 5, 6),
  Title = c("R Basics", "Python", "Statistics",
            "Data Science", "Java", "AI"),
  Author = c("Amit", "Raj", "Neha",
             "Kiran", "Priya", "John"),
  Genre = c("Education", "Technology", "Education",
            "Technology", "Programming", "Technology"),
  Price = c(450, 600, 550, 800, 400, 700),
  CopiesAvailable = c(10, 5, 8, 4, 12, 6)
)

# Step 2: Create CSV File
write.csv(library_data, "library.csv",
          row.names = FALSE)

# Step 3: Read CSV File
library <- read.csv("library.csv")

# Step 4: Display First Five Rows
print(head(library, 5))

# Step 5: Filter Books Price More Than 500
result <- library[library$Price > 500,
                  c("Title", "Author", "Price")]

print(result)

# Step 6: Group Books By Genre
average_price <- aggregate(
  Price ~ Genre,
  data = library,
  FUN = mean
)

print(average_price)

# Step 7: Create Histogram
hist(library$CopiesAvailable,
     main = "Available Book Copies",
     xlab = "Copies Available",
     ylab = "Frequency",
     col = "skyblue",
     border = "black")

# =========================================================================================================

# PAPER B - SPORTS DATA

# Step 1: Create Sports Data
sports_data <- data.frame(
  PlayerID = c(1, 2, 3, 4, 5, 6),
  Name = c("Virat", "Rohit", "Dhoni",
           "Sachin", "Gill", "Hardik"),
  Sport = c("Cricket", "Cricket", "Cricket",
            "Cricket", "Cricket", "Cricket"),
  Matches = c(100, 90, 80, 150, 60, 50),
  Runs = c(5000, 4500, 3000, 12000, 2000, 1500),
  Age = c(36, 38, 43, 51, 26, 32),
  Country = c("India", "India", "India",
              "India", "India", "India")
)

# Step 2: Create CSV File
write.csv(sports_data, "sports.csv",
          row.names = FALSE)

# Step 3: Read CSV File
sports <- read.csv("sports.csv")

# Step 4: Display First Three Rows
print(head(sports, 3))

# Step 5: Filter Players With More Than 1000 Runs
result <- sports[sports$Runs > 1000,
                 c("Name", "Sport", "Runs")]

print(result)

# Step 6: Group Players By Sport
average_runs <- aggregate(
  Runs ~ Sport,
  data = sports,
  FUN = mean
)

print(average_runs)

# Step 7: Create Line Plot
plot(sports$Runs,
     type = "o",
     col = "blue",
     main = "Runs of Each Player",
     xlab = "Player",
     ylab = "Runs",
     xaxt = "n")

axis(1,
     at = 1:nrow(sports),
     labels = sports$Name)

# =======================================================================================================

# PAPER C - ORDER DATA

# Step 1: Create Order Data
order_data <- data.frame(
  OrderID = c(1, 2, 3, 4, 5, 6),
  ProdNo = c(101, 102, 103, 104, 105, 106),
  ProdName = c("Pen", "Book", "Pencil",
               "Bag", "Scale", "Eraser"),
  Qty = c(10, 5, 20, 2, 8, 15),
  TotalBill = c(100, 250, 100, 1000, 80, 75)
)

# Step 2: Create CSV File
write.csv(order_data, "order.csv",
          row.names = FALSE)

# Step 3: Import CSV File
order <- read.csv("order.csv")

# Step 4: Display Complete Data
print(order)

# Step 5: Display First Five Rows
print(head(order, 5))

# Step 6: Display Data Structure
str(order)

# Step 7: Calculate Total Quantity Per Product
total_qty <- aggregate(
  Qty ~ ProdName,
  data = order,
  FUN = sum
)

print(total_qty)

# Step 8: Create Bar Chart
barplot(total_qty$Qty,
        names.arg = total_qty$ProdName,
        main = "Total Quantity Sold Per Product",
        xlab = "Product Name",
        ylab = "Total Quantity",
        col = "lightblue",
        border = "black")


# ====================================================================================================

# PAPER D - SQLITE DATABASE

# Step 1: Install Packages
install.packages("DBI")
install.packages("RSQLite")

# Step 2: Load Packages
library(DBI)
library(RSQLite)

# Step 3: Connect to SQLite Database
con <- dbConnect(SQLite(), "customer.db")

# Step 4: Create Customer Table
dbExecute(con, "
CREATE TABLE IF NOT EXISTS customer (
  CustID INTEGER,
  CustName TEXT,
  Bill REAL,
  City TEXT
)
")

# Step 5: Insert Sample Data
dbExecute(con, "
DELETE FROM customer
")

dbExecute(con, "
INSERT INTO customer VALUES
(1, 'Amit', 500, 'Surat'),
(2, 'Raj', 800, 'Mumbai'),
(3, 'Neha', 1200, 'Ahmedabad'),
(4, 'Kiran', 600, 'Vadodara'),
(5, 'Priya', 1500, 'Surat'),
(6, 'John', 900, 'Mumbai')
")

# Step 6: Import Customer Table
customer <- dbReadTable(con, "customer")

# Step 7: Display Complete Data
print(customer)

# Step 8: Display First Five Rows
print(head(customer, 5))

# Step 9: Display Data Structure
str(customer)

# Step 10: Create Histogram
hist(customer$Bill,
     main = "Histogram of Customer Bills",
     xlab = "Bill Amount",
     ylab = "Frequency",
     col = "lightgreen",
     border = "black")

# Step 11: Close Database Connection
dbDisconnect(con)


# ==================================================================================================
                                            All In One
# ==================================================================================================

# Create DataFrame
data <- data.frame()

# Create CSV
write.csv(data, "file.csv",
          row.names = FALSE)

# Read CSV
data <- read.csv("file.csv")

# First five rows
head(data, 5)

# Filter data
data[data$Price > 500, ]

# Calculate average
mean(data$Price)

# Calculate total
sum(data$Qty)

# Group data
aggregate(Price ~ Genre,
          data = data,
          FUN = mean)

# Histogram
hist(data$Price)

# Bar chart
barplot(data$Qty)

# Line graph
plot(data$Price, type = "o")

# SQLite connection
con <- dbConnect(SQLite(), "data.db")

# Import database table
data <- dbReadTable(con, "customer")

# Close connection
dbDisconnect(con)
