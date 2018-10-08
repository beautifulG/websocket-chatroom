<template>
	<div class="wrap-register">
		<p class="title">菜鸡聊天室</p>
		<div class="wrap-register-ipt">
			<input type="text" v-model.trim="nickname" placeholder="哥们，输个名字呗~">
		</div>
		<div class="wrap-chat-btn"><button class="chat-btn" @click="register(nickname)">开聊</button></div>
	</div>
</template>
<script type="text/javascript">
	export default{
		data(){
			return{
				nickname:'',
				id:'',
			}
		},
		mounted:function(){

		},
		methods:{
			register:function(nickname){
				this.$socket.emit('register', nickname);
				this.$router.push({ path: 'chat',query:{nickname:nickname}});
			}
		}
	}
</script>
<style type="text/css">
	.wrap-register{
		position: relative;
    	top: 100px;
    	margin-bottom: 50px;
    	width: 480px;
    	background-color: #ffffff;
    	box-shadow: 0 2px 3px 0 rgba(213,213,213,0.7);
    	margin: 0 auto;
    }
    .title{
    	font-family: serif;
	    font-size: 24px;
	    text-align: center;
	    color: #41464b;
	    -webkit-letter-spacing: 2px;
	    -moz-letter-spacing: 2px;
	    -ms-letter-spacing: 2px;
	    letter-spacing: 2px;
	    padding-top: 60px;
	    margin: 0 auto;
	    margin-bottom: 38px;
	    line-height: 30px;
	    width: 264px;
	    position: relative;
    }
    .wrap-register-ipt{position: relative;background: #f5f5f5;background-color: #f5f5f5;width: 296px;margin: 0 auto;}
    .wrap-register-ipt>input{
    	border: none;
    	height: 44px;
    	width: 100%;
    	padding: 12px 18px;
    	border-radius: 2px;
    	background-color: #f5f5f5;
    	box-sizing: border-box;
    	color: #41464b;
    	font-size: 14px;
    }
    .wrap-chat-btn{margin: 0px auto;width: 100px;padding: 40px;}
    .wrap-chat-btn>button{
    	box-sizing: border-box;
	    display: inline-block;
	    border-radius: 2px;
	    border-width: 1px;
	    border-style: solid;
	    background-color: #fff;
	    text-align: center;
	    -webkit-text-decoration: none;
	    text-decoration: none;
	    cursor: pointer;
	    -webkit-transition: opacity 0.3s,border-color 0.3s;
	    transition: opacity 0.3s,border-color 0.3s;
	    color: #fff;
	    border-color: #41464b;
	    background-image: linear-gradient(#41464b,#2c3033);
	    font-size: 14px;
	    font-weight: bold;
	    line-height: 1.4;
	    min-width: 100px;
	    height: 34px;
	    line-height: 32px;
	    padding: 0 15px;
    }
</style>