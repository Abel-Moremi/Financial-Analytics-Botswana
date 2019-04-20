function index(){

     let checkboxes = document.getElementsByClassName("indexStocks");
     let numberOfCheckedItems = 0;

     for(let i = 0; i < checkboxes.length; i++){
        if(checkboxes[i].checked)
        numberOfCheckedItems++;
     }
     if(numberOfCheckedItems > 3){
        M.toast({html: 'Choose 3 or less Domestic Stocks!', classes: 'rounded'});
        return false;
     }
}