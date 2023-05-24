<?php
header("Access-Control-Allow-Origin: *");
if(isset($_POST['url'])) {
    $site=$_POST['url'];
    $headers = get_headers($site);
    $html = $_POST['html'];
    $bytes=file_put_contents('markup.txt', $html);
    $decision=exec("F:/Malicious_Url_Detection/Sahi_Hai/venv/Scripts/python.exe test_run.py $site 2>&1 ");
    echo $decision;
} else {
    echo "url keys not present";
}
?>