CREATE DATABASE ${MYSQL_DATABASE};

USE ${MYSQL_DATABASE};
CREATE TABLE ${table1} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255),
    resume BLOB,
    cover_letter BLOB,
    additional_info TEXT,
    job VARCHAR(255)
);

CREATE TABLE {table2} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jobTitle VARCHAR(255),
    alias VARCHAR(255),
    jobDescription VARCHAR(255),
    locations VARCHAR(255),
    datePosted VARCHAR,
    jobType VARCHAR(50)
);
INSERT INTO ${table1} (firstName,lastName,phone,email,additional_info, job)
VALUES ("TestFN","TestLN","012-345-6789","example@example.com","kjefkjkjjrnj mkwknjwjnwkj wkjwkjrnjerknwtkjg njgwkjngkgrnkgte ektnjnekjnthnjethkjhtenj tekhetnjtjnethtkenjhekj hkjetjtejhtkj", "Software engineer");
INSERT INTO ${table1} (jobTitle,alias,jobDescription,locations, datePosted, jobType)
VALUES ("software_engineer","Software Engineer", "Building company software.", "City, State", "January, 1st, 2000", "Hybrid, Remote, In-Person");
