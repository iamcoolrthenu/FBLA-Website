<?php
require 'vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $mysqli = new mysqli(getenv('MYSQL_HOST'), getenv('USER'), getenv('MYSQL_PWD'), getenv('DB_NAME'));

    if ($mysqli->connect_errno) {
        die("Failed to connect to MySQL: " . $mysqli->connect_error);
    }

    // Sanitize user inputs
    $firstName = htmlspecialchars($mysqli->real_escape_string($_POST['firstName']));
    $lastName = htmlspecialchars($mysqli->real_escape_string($_POST['lastName']));
    $phone = htmlspecialchars($mysqli->real_escape_string($_POST['phone']));
    $email = htmlspecialchars($mysqli->real_escape_string($_POST['email']));
    $additional_info = htmlspecialchars($mysqli->real_escape_string($_POST['additional-info']));

    // File uploads
    $resume_tmp = $_FILES['resume']['tmp_name'];
    $cover_letter_tmp = $_FILES['cover-letter']['tmp_name'];

    // Validate file types
    $allowed_ext = ['doc', 'docx', 'pdf', 'txt'];
    $resume_ext = strtolower(pathinfo($_FILES['resume']['name'], PATHINFO_EXTENSION));
    $cover_letter_ext = strtolower(pathinfo($_FILES['cover-letter']['name'], PATHINFO_EXTENSION));

    if (!in_array($resume_ext, $allowed_ext) || !in_array($cover_letter_ext, $allowed_ext)) {
        echo "Error: Only Word, PDF, or TXT files are allowed for resumes and cover letters.";
        exit;
    }

    // Read file contents
    $resume_content = file_get_contents($resume_tmp);
    $cover_letter_content = file_get_contents($cover_letter_tmp);

    // Insert data into database
    $sql = "INSERT INTO ***REMOVED*** (firstName, lastName, phone, email, resume, cover_letter, additional_info) 
            VALUES (?, ?, ?, ?, ?, ?, ?)";
    
    $stmt = $mysqli->prepare($sql);
    $stmt->bind_param("ssssbbs", $firstName, $lastName, $phone, $email, $resume_content, $cover_letter_content, $additional_info);
    $stmt->send_long_data(4, $resume_content); // Bind resume content
    $stmt->send_long_data(5, $cover_letter_content); // Bind cover letter content

    if ($stmt->execute()) {
        // Execute external command (ensure it's properly secured and validated)
        $command = escapeshellcmd('/absolute/path/to/emailserver.py');
        $output = shell_exec($command);
        echo $output;

        // Redirect to a new page after successful submission
        header("Location: review.html");
        exit;
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close statement and connection
    $stmt->close();
    $mysqli->close();
}
?>
