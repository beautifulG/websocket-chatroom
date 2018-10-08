import App from '../App'

const register = r => require.ensure([], () => r(require('../pages/register')),'register')
const chat = r => require.ensure([], () => r(require('../pages/chat')),'chat')

export default [{
	path:'/',
	component:App,
	children:[
		{
            path: '',
            redirect: '/register'
        },
		{
			path:'/register',
			component:register
		},
		{
			path:'/chat',
			component:chat
		}
	]
}]
