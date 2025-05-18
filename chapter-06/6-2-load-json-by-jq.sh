jq -c 'group_by(.product) | map({
  product: .[0].product,                                                   
  total_sales: map(.quantity * .price) | add        
})' sales.json
