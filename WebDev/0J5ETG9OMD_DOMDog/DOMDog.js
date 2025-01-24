let is_image = false;
console.log("Heloo");
function onClickLikeButton() {
    if (is_image == false) {
        document.getElementById("puppyImage").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/white-puppy-liked-img.png";
        document.getElementById("likeIcon").style.color = "#0967d2";
        document.getElementById("likeButton").style.backgroundColor = "#0967d2";
        document.getElementById("likeButton").style.color = "#cbd2d9";
        is_image = true;

    } else {
        document.getElementById("puppyImage").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/white-puppy-img.png";
        document.getElementById("likeIcon").style.color = "#9aa5b1";
        document.getElementById("likeButton").style.backgroundColor = "#cbd2d9";
        document.getElementById("likeButton").style.color = "#9aa5b1";
        is_image = false;

    }
}