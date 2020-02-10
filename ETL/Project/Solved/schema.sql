-- Create Two Tables
CREATE TABLE temperature (
  id INT PRIMARY KEY,
  MonthTemp DATE,
  AvgTemp INT
);

CREATE TABLE drinking (
  id INT PRIMARY KEY,
  MonthRecorded DATE,
  MonthlySales INT
);