import boto3
import zipfile
import mimetypes
import StringIO

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:556855051476:deployPortfolioTopic')

    try: 
        s3 = boto3.resource('s3')
        portfolio_bucket = s3.Bucket('portfolio.stevebarronapps.info')
        build_bucket = s3.Bucket('portfoliobuild.stevebarronapps.info')
        
        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)
        
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
        
        topic.publish(Subject="portfolio deployed", Message="portfolio deployed")
    except:
        topic.publish(Subject="FAIL", Message="FAIL")

    return 'Hey Steve'