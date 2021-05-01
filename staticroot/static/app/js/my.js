$('.plus-cart').click(function(){
        var id =$(this).attr("pid").toString();
        var child1 = this.parentNode.children[2]
        console.log(id)
        console.log(child1)
        $.ajax({
            type:'GET',
            url:'/plus',
            data:{
                product_id:id
            },
            success:function(data){
                child1.innerText = data.quantity
                document.getElementById("mera").innerText = ""
                document.getElementById("totalamount").innerText  = "Total amount is this and place order Rs. "+data.price

                // document.getElementById("amount").innerText  = data.amount
                // document.getElementById("totalamount").innerText  = data.totalamount
            }
    
        })
    })
    $('.minus-cart').click(function(){
        var id =$(this).attr("pid").toString();
        var child1 = this.parentNode.children[1]
        var child2 = this.parentNode.children[2]
        var child3 = this.parentNode.children[3]
        var para;
        console.log(id)
        console.log(child1)
        console.log(child2)
        console.log(child3)
        $.ajax({
            type:'GET',
            url:'/minus',
            data:{
                product_id:id
            },
            success:function(data){
                console.log("Del")
                
                if (data.message == undefined)
                {
                    child2.innerText = data.quantity
                    document.getElementById("totalamount").innerText  = "Total amount is this and place order Rs. "+data.price

                }
                else
                {
                    child2.innerText = data.quantity
                    document.getElementById("mera").innerText  = data.message
                     document.getElementById("amount").innerText  = data.amount
                     document.getElementById("totalamount").innerText  = "Total amount is this and place order Rs. "+data.price

                }

                
            }
    
        })
    })

    $('.remove-cart').click(function(){
        var id =$(this).attr("pid").toString();
        var child1 = this.parentNode.children[1]
        var child2 = this.parentNode.children[2]
        var child3 = this.parentNode.children[3]
        console.log(id)
        console.log(child1)
        console.log(child2)
        console.log(child3)
        $.ajax({
            type:'GET',
            url:'/remove',
            data:{
                product_id:id
            },
            success:function(data){

                console.log("Rem")

                document.getElementById("totalamount").innerText  = "Total amount is this and place order Rs. "+data.price

                child1.parentNode.parentNode.parentNode.parentNode.remove()
                
            }
    
        })
    })