<template>
	<div class="wrap-chatroom">
		<p class="chatroom-title">来聊5毛钱的天~</p>
		<vue-scroll :ops="ops">
			<div class="chat-body mt5">
				<div v-for="(item,index) of msgs" :key="index">
					<div v-if="item.msgType == 'register'" class="chat-tip mt5">
						<span>{{ item.username + item.statusTxt}}</span>
					</div>
					<div v-else>
						<div v-if="item.username == $route.query.nickname" class="self mt5"  style="text-align:right;">
							<div class="user">{{ item.username }}</div>
							<div class="bubble mt5">
								<span class="chatBubble">{{ item.msg }}</span>
							</div>
						</div>
						<div v-else class="others mt5">
							<div class="user">{{ item.username }}</div>
							<div class="bubble mt5">
								<span class="chatBubble">{{ item.msg }}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</vue-scroll>
		<div class="wrap-btn" style="padding-top:5px;">
			<input class="chat-ipt" type="text" placeholder="说点撒吧？...." v-model.trim="msg">
            <a class="msg-btn" href="javascript:" @click="sentMessage(msg)">发送</a>
		</div>
	</div>
</template>

<script type="text/javascript">
	export default{
		data(){
			return{
				msgs: [],
				ops:{
					bar:{
						background: "rgba(247, 247, 247, 0)"
					}
				}
			}
		},
		mounted:function(){
			// 用户上线提醒
			this.$socket.on("register", data => {
				this.msgs.push({
			        msgType: "register",
			        username: data.nickname,
			        statusTxt:"进来唠嗑了",
			    });
			});
			// 接收消息
		    this.$socket.on("msg", data => {
			    this.msgs.push({
			    	msgType: "msg",
			        username: data.nickname,
			        msg: data.msg
			    });
		    });
		    // 用户下线提醒
		    this.$socket.on("quit", data => {
		        this.msgs.push({
			        msgType: "quit",
			        username: data.nickname
		      	});
		    });
		},
		methods:{
			sentMessage:function(msg){
				this.msg="";
				this.$socket.emit('msg', msg);
			}
		}
	}
</script>
<style type="text/css">
	.mt5{margin-top: 5px;}
	.wrap-chatroom{
		position: relative;
    	top: 100px;
    	margin-bottom: 50px;
    	width: 480px;
    	background-color: #ffffff;
    	box-shadow: 0 2px 3px 0 rgba(213,213,213,0.7);
    	margin: 0 auto;
    }
	.chatroom-title{
    	font-family: serif;
	    font-size: 24px;
	    color: #41464b;
	    -webkit-letter-spacing: 2px;
	    -moz-letter-spacing: 2px;
	    -ms-letter-spacing: 2px;
	    letter-spacing: 2px;
	    padding: 15px;
	    border-bottom: 1px solid #e2e2e2;
	    line-height: 30px;
	    width: 390px;
	    position: relative;
	    margin: 5px auto;
    }
    .chat-body{
    	width: 420px;
    	margin: 0 auto;
    	height: 300px;
    }
    .wrap-chat-ipt{position: relative;background: #f5f5f5;background-color: #f5f5f5;width: 296px;margin: 0 auto;}
    .chat-ipt{
    	border: none;
    	height: 44px;
    	width: 100%;
    	padding: 12px 18px;
    	border-radius: 2px;
    	background-color: #f5f5f5;
    	box-sizing: border-box;
    	color: #41464b;
    	font-size: 14px;
    	outline: none;
    }
    .wrap-btn{display: flex;display: -webkit-flex;}
    .msg-btn{
    	box-sizing: border-box;
	    display: inline-block;
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
	    height: 44px;
	    line-height: 42px;
	    padding: 0 15px;
		flex: 0 0 100px;
		-webkit-flex: 0 0 100px;
	}
	.user{
		font-size: 14px;
		font-family: serif;
		color: #a0a2a5;
		line-height: 20px;
	}
	.chatBubble{
		border-radius: 5px !important;
		background: #E0EDFF;
		padding: 5px 12px;
		font-size: 15px;
	}
	.chat-tip{text-align: center;}
	.chat-tip>span{
		background: #f5f5f5;
		font-size: 12px;
		height: 25px;
		display: inline-block;
		line-height: 25px;
		padding: 0 10px;
		border-radius: 4px;
		color: #41464b;
	}
</style>