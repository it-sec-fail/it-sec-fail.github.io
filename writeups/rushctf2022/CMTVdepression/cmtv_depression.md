# CMTV Depression 1 and 2

Medium

## Challenge description

[https://t.ly/Z_wg4](https://t.ly/Z_wg4)

Find the murder house, what is the event being advertised? That's flag1!

For extra points, what about the TV show and season number?
That's flag2!

Flag: `RUSH{ALLCAPSMESSAGE}`

> RUSH{REVENGEOFTHE90S}

## Solving

The link will open a news-page, that shows an article about a murder. In the video (embedded in the website) we can see the number of the house(97) and in the article we can get the street and city of the family that were attacked. So we have everthing for some google action.

Here is a picture of the video and the house number
![Picture of the embedded video and the house number](video.png)
And here is the article
![Picture of the articel](article.png)

So the address we need to google should be:

> Av. Pinhal do Vidal 97, Portugal

![Google Request](google_request.png)

Okay let's open Google Street View on the address and look around. If we look closely we can see a busstop. There is a poster for an event. This should be the first flag!

![Busstop](busstop.png)
![Poster of the event](busstop_lose_flag1.png)

> RUSH{REVENGEOFTHE90S}

### Second flag

We can find the second flag on the other side of the busstop poster. 
Just go to the next Google Street View point and look at the busstop poster.

![Poster of the TV Show](flag2.png)

Sadly I cannot really guess what TV show this would be... but it looks kind of familier. I took the picture snippet and posted it in the google image search.

![Google Request for TV show](google_tv_show.png)

Yeah. Stranger Things... season 4. I love stranger things. :-)

![Stranger Things poster](stranger_things.jpg)

> RUSH{STRANGERTHINGS4}