<?php
header("Access-Control-Allow-Origin: *");
if(isset($_POST['url'])) {
    $site=$_POST['url'];
    #$headers = get_headers($site);
    #print_r($site);
    #$html = file_get_contents($site);
    #$bytes=file_put_contents('markup.txt', $html);
    $decision=exec("F:/Sanchalak/venv/Scripts/python.exe test_run.py $site 2>&1 ");
    echo $decision;
} else {
    echo "url keys not present";
}
?>