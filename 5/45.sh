#!/bin/sh

echo 'コーパス中で頻出する述語と格パターンの組み合わせ'
awk '{ cnt[$1 " " $2]++ }
END{
    for( pair in cnt ) {
        print pair " " cnt[pair]
    }
}' 45.txt | sort -k 3 -nr | head -20

echo ''

echo '「する」「見る」「与える」という動詞の格パターン'
awk '{
    if($1 == "する" || $1 == "見る" || $1 == "与える") {
        cnt[$1 " " $2]++
    }
}
END {
    for( pair in cnt ) {
        print pair " " cnt[pair]
    }
}' 45.txt | sort -k 3 -nr

