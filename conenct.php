<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Database connection
    $mysqli = new mysqli('localhost', '***REMOVED***', '***REMOVED***', '***REMOVED***');

    // Check connection
    if ($mysqli->connect_errno) {
        die("Failed to connect to MySQL: " . $mysqli->connect_error);
    }

    // Escape user inputs for security
    $name = $mysqli->real_escape_string($_POST['name']);
    $phone = $mysqli->real_escape_string($_POST['phone']);
    $email = $mysqli->real_escape_string($_POST['email']);
    $additional_info = $mysqli->real_escape_string($_POST['additional-info']);

    // File uploads
    $resume = $_FILES['resume']['name'];
    $resume_tmp = $_FILES['resume']['tmp_name'];
    $resume_path = "uploads/" . $resume;
    move_uploaded_file($resume_tmp, $resume_path);

    $cover_letter = $_FILES['cover-letter']['name'];
    $cover_letter_tmp = $_FILES['cover-letter']['tmp_name'];
    $cover_letter_path = "uploads/" . $cover_letter;
    move_uploaded_file($cover_letter_tmp, $cover_letter_path);
    //echo "Thank you, $name, for your application!";
    // Insert data into database
    $sql = "INSERT INTO ***REMOVED*** (name, phone, email, resume, cover_letter, additional_info) 
            VALUES ('$name', '$phone', '$email', '$resume_path', '$cover_letter_path', '$additional_info')";
    header("Location: review.html");
    if ($mysqli->query($sql) === true) {
        // Redirect to a new page after successful submission
        echo "Working"
        header("Location: review.html");
        exit;
    } else {
        echo "Error: " . $sql . "<br>" . $mysqli->error;
    }

    // Close connection
    $mysqli->close();
}
?>
