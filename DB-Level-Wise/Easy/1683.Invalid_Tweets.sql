# Write your MySQL query statement below
select tweet_id
from tweets
where char_length(content) > 15 ##char return the length of the character

#Length () -> use to return string length in bytes
#char_length() -> use to return string length in characcter