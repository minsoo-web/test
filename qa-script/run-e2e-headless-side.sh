lst_eng=(`find /root/IRIS-E2E-SAAS/IRIS-E2E-SAAS-ENG/ -type f -name '*.side' -and ! -name '*SETUP*.side'`)

echo [`date +%Y/%m/%d/%H%M`]
echo IRIS-E2E-SAAS HEADLESS TEST SIDE START

for name_eng in ${lst_eng[*]}
do
    echo SIDE file is : ${name_eng}
	selenium-side-runner -c "goog:chromeOptions.args=[headless,no-sandbox] browserName=chrome" $name_eng --output-directory=/root/IRIS-E2E-SAAS/qa-report --output-format=junit >> temp.txt
    sleep 10
done

echo IRIS-E2E HEADLESS SIDE TEST DONE