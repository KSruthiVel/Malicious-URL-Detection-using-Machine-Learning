<div align="center">
 <h1> Malicious URL Detection using Machine Learning </h1>
</div>
<div align="justify">
The rise of malicious activities on the World Wide Web poses a threat to users' sensitive information. In 2021, half of all cybercrime victims were targeted by phishing attacks, demonstrating the scale of the problem. The consequences of falling victim to a phishing attack can be severe, including financial loss, identity theft, and reputational damage. <br> <br>
It is a common misconception that if there is a padlock symbol next to the website URL, the site is always safe. The padlock icon only indicates that the communication between the user's browser and the website is encrypted, which helps protect the data from eavesdropping or interception. Scammers previously didn't bother with digital certificates for fake websites, making them easier to spot. However, scammers have become more sophisticated, using fake certificates or exploiting legitimate sites. While the padlock symbol is helpful, users should verify authenticity through other means like checking the URL and trust indicators. <br> <br>
 </div>
 
![image](https://github.com/KSruthiVel/Malicious_URL_Detection_using_ML/assets/68786151/d965f852-6f2a-4268-a460-2ff7aa0d0c1f)

## Features
#### Lexical Features
These refer to statistical features extracted from the literal URL string. For example, length of the URL string, 
number of digits, number of parameters in its query part, if the URL is encoded, etc. Example, ‘amazon.com.support.info’.

#### Host-Based Features
These provide information about the host of the webpage, for example, country of registration, domain name properties, 
named servers, connection speed, time to live from registration, etc. The motivation behind including these parameters 
is that there is a difference in website deployment tactics, the longevity of existence, and the reputation for malicious and benign sites.

#### Content Features
These are obtained from the downloaded HTML code of the webpage. These features capture the structure of the webpage and 
the content embedded in it. These will include information on script tags, embedded objects, executables, hidden elements, etc. 
For example, in an SQL injection attack, anomalies such as malformed documents or repeated tags show up in raw HTML content.

<table>
    <thead>
        <tr>
            <th>Lexical Features</th>
            <th>Host-based Features</th>
            <th>Content-based Features</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>url_of_anchor</td>
            <td>registration_length</td>
            <td>web_traffic</td>
        </tr>
        <tr>
            <td>sub_domain</td>
            <td>age_of_domain</td>
            <td>favicon</td>
        </tr>
        <tr>
            <td>having_-</td>
            <td>having_ip</td>
            <td>redirect</td>
        </tr>
        <tr>
            <td>links_in_tags</td>
            <td>google_index</td>
            <td>submitting_to_email</td>
        </tr>
        <tr>
            <td>sfh</td>
            <td>dns_record</td>
            <td>statistical_report</td>
        </tr>
        <tr>
            <td>request_url</td>
            <td></td>
            <td>mouse_over</td>
        </tr>
        <tr>
            <td>url_length</td>
            <td></td>
            <td>iframe</td>
        </tr>
        <tr>
            <td>https_token</td>
            <td></td>
            <td>rightclick</td>
        </tr>
        <tr>
            <td>shortening_service</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>having_@</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>abnormal_url</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>having_//</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

## Flowchart
 ![activity diagram](https://github.com/KSruthiVel/Malicious_URL_Detection_using_ML/assets/68786151/6a8cd9c0-6e5d-4a0b-b441-87332128faea)

## Tech Stack

**UI:** HTML5, CSS3.

**Backend:** Python3.

**Libraries:** beautifulsoup4, googlesearch-python, scikit-learn, pandas, requests, whois.

## Screnshots
![image](https://github.com/KSruthiVel/Malicious_URL_Detection_using_ML/assets/68786151/d0061035-477d-401f-b3ab-e1b03a69f974)
![image](https://github.com/KSruthiVel/Malicious_URL_Detection_using_ML/assets/68786151/cb4ac0d2-d15f-4052-a82d-2f54f8e7c85e)
![image](https://github.com/KSruthiVel/Malicious_URL_Detection_using_ML/assets/68786151/10536fc7-a429-4336-843d-fa040b0e0956)
![image](https://github.com/KSruthiVel/Malicious_URL_Detection_using_ML/assets/68786151/89a6b471-d84b-47ff-ac25-4b7194344743)

## Future Scope
<div align="jusitfy">
The developed model for malicious URL detection exhibits impressive results, but improvement is needed, particularly in reducing the prediction time of 30 seconds for real-time detection. Another area for improvement is to handle situations where a website is down or permission to access it is denied. In such circumstances, the current model cannot predict whether the website is malicious or not. This limitation can be addressed by incorporating additional features that can be extracted from other sources, such as WHOIS data or passive DNS information.
  </div>
