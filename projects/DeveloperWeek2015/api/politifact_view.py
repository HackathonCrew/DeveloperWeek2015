def returnPolitifact(request):
    return HttpResponse(getPolitiafct())

def getPolitifact():
    statement = {

        "statement_url": "http://www.politifact.com/truth-o-meter/statements/2015/feb/03/barack-obama/barack-obama-says-politicians-get-credit-founding-/", 
        "target": [], 
        "statement_date": "2015-01-22", 
        "statement_context": "an interview with YouTube celebrity Bethany Mota", 
        "speaker": {
            "party": {
                "party": "Democrat", 
                "party_slug": "democrat"
            }, 
            "first_name": "Barack", 
            "last_name": "Obama", 
            "name_slug": "barack-obama", 
            "canonical_photo": "http://static.politifact.com.s3.amazonaws.com:80/mugs%2Fmug-barackobama.jpg"
        }, 
        "ruling_headline": "Barack Obama says politicians get credit for founding colleges", 
        "statement": "<p>&quot;The reason we even have colleges is that at some point there were politicians who said, &lsquo;You know what? We should start colleges.&rsquo; &quot;</p>\r\n", 
        "ruling": {
            "ruling_slug": "barely-true", 
            "ruling": "Mostly False", 
            "canonical_ruling_graphic": "http://static.politifact.com.s3.amazonaws.com:80/rulings%2Ftom-mostlyfalse.gif"
        }, 
        "ruling_link_text": "Way oversimplified", 
        "ruling_date": "2015-02-03 10:34:14", 
        "statement_type": {
            "statement_type": "Claim"
        }, 
        "subject": [
            {
                "subject_slug": "education", 
                "subject": "Education"
            }, 
            {
                "subject_slug": "history", 
                "subject": "History"
            }
        ]
    }

    return json.dumps(statement)

