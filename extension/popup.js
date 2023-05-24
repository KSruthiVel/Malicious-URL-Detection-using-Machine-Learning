function transfer() {
  var tablink;
  chrome.tabs.getSelected(null, function (tab) {
    const original_url = tab.url
    console.log(original_url);
    // alert(original_url);
    tablink = tab.url;
    if (tablink.length > 30) {
      tablink = tablink.slice(0, 30) + ' ...';
    }
    $('#site').text(tablink);

    var xhr = new XMLHttpRequest();
    params = 'url=' + original_url;
    var markup =
      'url=' + original_url + '&html=' + document.documentElement.innerHTML;
	xhr.open("POST","http://localhost:8000",true);
    //alert(xhr.status);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send(markup);
    $('#loader').removeClass('hidden'); // Show the spinner
    xhr.onload = () => {
      // alert(xhr.responseText);
       $('#loader').addClass('hidden'); // Hide the spinner
      if (xhr.responseText === 'SAFE') {
        $('#div1').text(xhr.responseText);
      } else {
        $('#div2').text(xhr.responseText);
      }
      return xhr.responseText;
    };

  });
}

function hello(){
   console.log("Hello");
}
$(document).ready(function () {
  $('button').click(function () {
    var val = transfer();
    // hello();
  });
});

chrome.tabs.getSelected(null, function (tab) {
  var tablink = tab.url;
  if (tablink.length > 30) {
    tablink = tablink.slice(0, 30) + ' ....';
  }
  $('#site').text(tablink + '\n\n');
});
