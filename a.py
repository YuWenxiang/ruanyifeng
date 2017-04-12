#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        print(data)
        
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
        handle_data(self, data)
        #print('--**%s**--'%attrs)

    #def handle_endtag(self, tag):
     #   print('</%s>' % tag)

   #def handle_startendtag(self, tag, attrs):
    #    print('<%s/>' % tag)



    #def handle_comment(self, data):
     #   print('<!--', data, '-->')

    #def handle_entityref(self, name):
     #   print('&%s;' % name)

    #def handle_charref(self, name):
     #   print('&#%s;' % name)
     

parser = MyHTMLParser()
parser.feed('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" id="sixapart-standard">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="generator" content="Movable Type  5.2.2" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="stylesheet" href="http://www.ruanyifeng.com/blog/styles.css" type="text/css" />
<link rel="start" href="http://www.ruanyifeng.com/blog/" title="Home" />
<link rel="alternate" type="application/atom+xml" title="Recent Entries" href="http://feeds.feedburner.com/ruanyifeng" />
<script type="text/javascript" src="http://www.ruanyifeng.com/blog/mt.js"></script>
<!--
<rdf:RDF xmlns="http://web.resource.org/cc/"
         xmlns:dc="http://purl.org/dc/elements/1.1/"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<Work rdf:about="http://www.ruanyifeng.com/blog/2017/03/pointfree.html">
<dc:title>Pointfree 编程风格指南</dc:title>
<dc:description>本文要回答一个很重要的问题：函数式编程有什么用？...</dc:description>
<dc:creator>阮一峰</dc:creator>
<dc:date>2017-03-13T06:56:10+08:00</dc:date>
<license rdf:resource="http://creativecommons.org/licenses/by-nc-nd/3.0/" />
</Work>
<License rdf:about="http://creativecommons.org/licenses/by-nc-nd/3.0/">
</License>
</rdf:RDF>
-->


    
    <link rel="prev" href="http://www.ruanyifeng.com/blog/2017/03/ramda.html" title="Ramda 函数库参考教程" />
    <link rel="next" href="http://www.ruanyifeng.com/blog/2017/03/reduce_transduce.html" title="Reduce 和 Transduce 的含义" />
    
    <title>Pointfree 编程风格指南 - 阮一峰的网络日志</title>
</head>
<body id="scrapbook" class="mt-entry-archive one-column">
<script>
if (/mobile/i.test(navigator.userAgent) || /android/i.test(navigator.userAgent)) document.body.classList.add('mobile');

window.addEventListener('load', function(event) {
  setTimeout(function () {
    hab('#sup-post-2');
    hab('#gd1-inner');
  }, 1000);
});
</script>
    <div id="container">
        <div id="container-inner">

            <div id="header">
    <div id="header-inner">
        <div id="header-content">


            <div id="header-name">阮一峰的网络日志 <span id="site_location"> » <a href="http://www.ruanyifeng.com/blog/" accesskey="1">首页</a></span><span id="site_archive"> » <a href="http://www.ruanyifeng.com/blog/archives.html">档案</a></span>
</div>

<div id="google_search">
<!-- SiteSearch Google -->
<form action="http://www.ruanyifeng.com/blog/search.html" id="cse-search-box">
      <div>
        <input type="hidden" name="cx" value="016304377626642577906:b_e9skaywzq" />
    <input type="hidden" name="cof" value="FORID:11" />
    <input type="hidden" name="ie" value="UTF-8" />
        <input type="text" name="q" size="20" class="searchbox" id="sbi" value=""/>
        <input type="image" src="/static/themes/theme_scrapbook/images/top_search_submit.gif" class="searchbox_submit" value="" alt="搜索" name="sa"/>
      </div>
    </form>
<!-- SiteSearch Google -->
</div>
<div id="feed_icon">
<a href="/feed.html" title="订阅Feed">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAUzSURBVHjavFdbbFRVFF3nPjoz7dTWTittaW0jUDRAUqaNojyqREnEQKgfUj9MqqAmhqRt/OCD4CuY+Kckoh+aiGKC+gMJbdHoRysJ8dkhhmJLNdDKtJU+6GMK87j3Hs85d2Z6HzNtMYWb3Dn3NWftvfba+5xNYDl+e6Fkj6yqb/oDRbWq14vlPBLRKCITkxf0ROLt+hNjp1PPSRK4kA3vF1dXNRcWlyA2OQU9eos9opAkAiKxD+XkKO6t15aRWO7J/MgmAZU8MEgexgZHMX518Dh72sYMmVKShnxWuWHdHtxKIDIYTgMuDzgfmSOIQkYMpdUF8OY92Hytt4/jvkg47czzU16iQovM3QFwmNck+Yyduu7D6NA0Z6JR4THntFs9V4tWQg6Ui3s6MwKDncsFTnXKLJhDSeUK3AgPtyhccDzmVs999buRt/1Vm4i0od+hX7+MRG87jPGB/w1u8FPj9xEw7McVrnYuOCvtpjTth3J/nTg99c8LRhKhr6D3dTB5R24bXFwbMXBsyZzeoXaycEpJ95TB09AGX/NpqLVNtw8urnVzLvHjFNxiFqRy2OOHuqUVnue+ACkoWzo4O6lGzTmuHq6nPvY2m9rVqjrIK2rMEKxqyG5NPAKt+wjo0LklgfNxJkZMA3KJvqRUk3z5UFY3QH14P0h+WUY79HPvgv7VuSg4ZRGY1YgZgqXmORccF17sy2ehnf9AeO085K2HQFbtXBScj0LcpgF2cN+WV+DZ/LJQu6gD4R7oV7pBJwbSgtMvfiPoVp56DySwxm7EtkMs1WdAB7qzggsDJKQYsHucSkOudrkiCPWR/fA2nYCn8SNIK4NptSMyAu3sAdDRkIsJdfth0LzSrODUoPNZ4KI9SxJI5UHk7D4GdQfz2us31c7CoHMjRkKuDPHseCMrONVhNcDJwMJpKFVvg9L4OaTiNWm1x789KCqkrXhVBiEz0WYCT2nAzQAD1/vaETv1GrRfP4Vx5cfMNcDPwvP0h0DhanPym7OIf/+O67vcJ1/PCJ4KgdzaUP6Wz+dU+5yIL6fV+PsHGAOdwlPpvvUOyeeAVGyCdqkDNB6DPjsBSrnndfOGevOh3RhGItxvA+fX1CtbGFhgYUFkFMZPR6F1HnClHq8HyubWtJexX06CRmdt33hrd7nA7SFY4qoGpnYuOKcRykPPgDCBcsHx9Iv+fNL2PueBehCWUfYQIIMGLOCcOmXDXsh1+yCt35tUPfvzGFuSvzvoinXOxqa02qOhM6733nVP2MAdaej2XN11DPKjLZCD+yBvahGCo7JfTKAN9UD7s8Oe9zUNIhz8fWI8DG2k38WCFdxugANcXrvTVd1IEbuv3Jour7Hzn7jLMBNfKs7R3i67gRVrbeCOEDhinmWhAatsqdquM2XzHZINhK2cqTjHr/XZdVJUbgN3MWAVXKbSyg9jesRW2xP9di+lwrL5ojM3m2H/kG9hwcIA37c71W6wJdW2J2S5nrjYbq/t1AHAhJsKQeyfPvf6IMJgghPJhFZ4x0KlfLFvt22du45Au/A1SOlGc0P672XXwhLtOcM0kTTEMMd0qkVmMNXxMd/tsedUjInr4SQDgOfeXMSiN0FCL5WHah4L1qqYXPJOJlttd+a5M+YpcG5poLYKQ5f+6JJ4r8bbJYP47hq4r7QAs9PjYNhHJd4o8l5taiwuOpa7AS4XKqI/5NjJbTnaWK92nLdLuhQAJayRNMiygXPBeQN+Qbvu0zDc3y+aUzhbkGR73sI7ljvUnndx2q3t+X8CDAD66FtrIL864AAAAABJRU5ErkJggg==" alt="" style="border: 0pt none;" />
</a></div>

        </div>
    </div>
</div>



            <div id="content">
                <div id="content-inner">


                    <div id="alpha">
                        <div id="alpha-inner">


                            <div id="entry-1925" class="entry-asset asset hentry">
                                <div class="asset-header">
<div class="asset-nav entry-nav">

<div class="entry-location">
<ul>
<li>上一篇：<a href="http://www.ruanyifeng.com/blog/2017/03/ramda.html" title="Ramda 函数库参考教程">Ramda&nbsp;函数库参考</a></li>
<li>下一篇：<a href="http://www.ruanyifeng.com/blog/2017/03/reduce_transduce.html" title="Reduce 和 Transduce 的含义">Reduce&nbsp;和&nbsp;Tr</a></li>
</ul>
</div>


    
                                    <div class="entry-categories">
                                        <p>分类<span class="delimiter">：</span></p>
                                        <ul>
                                            <li><a href="http://www.ruanyifeng.com/blog/javascript/" rel="tag">JavaScript</a></li>
                                        </ul>
                                    </div>
    


                                            
</div>
                                </div>
<article class="hentry">
                                    <h1 id="page-title" class="asset-name entry-title">Pointfree 编程风格指南</h1>
                                            <div id="share_button" style="float:right;padding-right:2em;padding-top:1em;"></div>
                                    <div class="asset-meta">
                                        

                                            <p class="vcard author">作者： <a class="fn url" href="http://www.ruanyifeng.com">阮一峰</a></p>
                                    <p>日期： <a href="http://www.ruanyifeng.com/blog/2017/03/"><abbr class="published" title="2017-03-13T06:56:10+08:00">2017年3月13日</abbr></a></p>


                                    </div>
                                
                                <div class="asset-content entry-content" id="main-content">

                                    <!-- div class="asset-body" -->
                                        <p>本文要回答一个很重要的问题：<a href="http://www.ruanyifeng.com/blog/2017/02/fp-tutorial.html">函数式编程</a>有什么用？</p>

                                    <!-- /div -->


                                    <!-- div id="more" class="asset-more" -->
                                        <p>目前，主流的编程语言都不是函数式的，已经能够满足需求。为何还要学函数式编程呢，只为了多理解一些新奇的概念？</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031201.jpg" alt="" title="" /></p>

<p>一个网友说：</p>

<blockquote>
  <p>"函数式编程有什么优势呢？"</p>

<p>"我感觉，这种写法可能会令人头痛吧。"</p>
</blockquote>

<p>很长一段时间，我根本不知道从何入手，如何将它用于实际项目？直到有一天，我学到了 Pointfree 这个概念，顿时豁然开朗，原来应该这样用！</p>

<p>我现在觉得，Pointfree 就是如何使用函数式编程的答案。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031210.jpg" alt="" title="" /></p>

<h2>一、程序的本质</h2>

<p>为了理解 Pointfree，请大家先想一想，什么是程序？</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031202.png" alt="" title="" /></p>

<p>上图是一个编程任务，左侧是数据输入（input），中间是一系列的运算步骤，对数据进行加工，右侧是最后的数据输出（output）。<strong>一个或多个这样的任务，就组成了程序。</strong></p>

<p>输入和输出（统称为 I/O）与键盘、屏幕、文件、数据库等相关，这些跟本文无关。<strong>这里的关键是，中间的运算部分不能有 I/O 操作，应该是纯运算，即通过纯粹的数学运算来求值。</strong>否则，就应该拆分出另一个任务。</p>

<p>I/O 操作往往有现成命令，大多数时候，编程主要就是写中间的那部分运算逻辑。现在，主流写法是过程式编程和面向对象编程，但是我觉得，最合适纯运算的是函数式编程。</p>

<h2>二、函数的拆分与合成</h2>

<p>上面那张图中，运算过程可以用一个函数<code>fn</code>表示。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031203.png" alt="" title="" /></p>

<p><code>fn</code>的类型如下。</p>

<blockquote><pre><code class="language-javascript">
fn :: a -> b
</code></pre></blockquote>

<p>上面的式子表示，函数<code>fn</code>的输入是数据<code>a</code>，输出是数据<code>b</code>。</p>

<p>如果运算比较复杂，通常需要将<code>fn</code>拆分成多个函数。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031204.png" alt="" title="" /></p>

<p><code>f1</code>、<code>f2</code>、<code>f3</code>的类型如下。</p>

<blockquote><pre><code class="language-javascript">
f1 :: a -> m
f2 :: m -> n
f3 :: n -> b
</code></pre></blockquote>

<p>上面的式子中，输入的数据还是<code>a</code>，输出的数据还是<code>b</code>，但是多了两个中间值<code>m</code>和<code>n</code>。</p>

<p>我们可以把整个运算过程，想象成一根水管（pipe），数据从这头进去，那头出来。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031205.png" alt="" title="" /></p>

<p>函数的拆分，无非就是将一根水管拆成了三根。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031206.png" alt="" title="" /></p>

<p>进去的数据还是<code>a</code>，出来的数据还是<code>b</code>。<code>fn</code>与<code>f1</code>、<code>f2</code>、<code>f3</code>的关系如下。</p>

<blockquote><pre><code class="language-javascript">
fn = R.pipe(f1, f2, f3);
</code></pre></blockquote>

<p>上面代码中，我用到了 <a href="http://www.ruanyifeng.com/blog/2017/03/ramda.html">Ramda</a> 函数库的<a href="http://ramdajs.com/docs/#pipe"><code>pipe</code></a>方法，将三个函数合成为一个。Ramda 是一个非常有用的库，后面的例子都会使用它，如果你还不了解，可以先读一下<a href="http://www.ruanyifeng.com/blog/2017/03/ramda.html">教程</a>。</p>

<h2>三、Pointfree 的概念</h2>

<blockquote><pre><code class="language-javascript">
fn = R.pipe(f1, f2, f3);
</code></pre></blockquote>

<p>这个公式说明，如果先定义<code>f1</code>、<code>f2</code>、<code>f3</code>，就可以算出<code>fn</code>。整个过程，根本不需要知道<code>a</code>或<code>b</code>。</p>

<p>也就是说，我们完全可以把数据处理的过程，定义成一种与参数无关的合成运算。不需要用到代表数据的那个参数，只要把一些简单的运算步骤合成在一起即可。</p>

<p><strong>这就叫做 Pointfree：不使用所要处理的值，只合成运算过程。</strong>中文可以译作"无值"风格。</p>

<p>请看下面的例子。</p>

<blockquote><pre><code class="language-javascript">
var addOne = x => x + 1;
var square = x => x * x;
</code></pre></blockquote>

<p>上面是两个简单函数<code>addOne</code>和<code>square</code>。</p>

<p>把它们合成一个运算。</p>

<blockquote><pre><code class="language-javascript">
var addOneThenSquare = R.pipe(addOne, square);

addOneThenSquare(2) //  9
</code></pre></blockquote>

<p>上面代码中，<code>addOneThenSquare</code>是一个合成函数。定义它的时候，根本不需要提到要处理的值，这就是 Pointfree。</p>

<h2>四、Pointfree 的本质</h2>

<p>Pointfree 的本质就是使用一些通用的函数，组合出各种复杂运算。上层运算不要直接操作数据，而是通过底层函数去处理。这就要求，将一些常用的操作封装成函数。</p>

<p>比如，读取对象的<code>role</code>属性，不要直接写成<code>obj.role</code>，而是要把这个操作封装成函数。</p>

<blockquote><pre><code class="language-javascript">
var prop = (p, obj) => obj[p];
var propRole = R.curry(prop)('role');
</code></pre></blockquote>

<p>上面代码中，<code>prop</code>函数封装了读取操作。它需要两个参数<code>p</code>（属性名）和<code>obj</code>（对象）。这时，要把数据<code>obj</code>要放在最后一个参数，这是为了方便柯里化。函数<code>propRole</code>则是指定读取<code>role</code>属性，下面是它的用法（查看<a href="http://jsbin.com/nevuje/edit?js,console">完整代码</a>）。</p>

<blockquote><pre><code class="language-javascript">
var isWorker = s => s === 'worker';
var getWorkers = R.filter(R.pipe(propRole, isWorker));

var data = [
  {name: '张三', role: 'worker'},
  {name: '李四', role: 'worker'},
  {name: '王五', role: 'manager'},
];
getWorkers(data)
// [
//   {"name": "张三", "role": "worker"},
//   {"name": "李四", "role": "worker"}
// ]
</code></pre></blockquote>

<p>上面代码中，<code>data</code>是传入的值，<code>getWorkers</code>是处理这个值的函数。定义<code>getWorkers</code>的时候，完全没有提到<code>data</code>，这就是 Pointfree。</p>

<p>简单说，Pointfree 就是运算过程抽象化，处理一个值，但是不提到这个值。这样做有很多好处，它能够让代码更清晰和简练，更符合语义，更容易复用，测试也变得轻而易举。</p>

<h2>五、Pointfree 的示例一</h2>

<p>下面，我们来看一个示例。</p>

<blockquote><pre><code class="language-javascript">
var str = 'Lorem ipsum dolor sit amet consectetur adipiscing elit';
</code></pre></blockquote>

<p>上面是一个字符串，请问其中最长的单词有多少个字符？</p>

<p>我们先定义一些基本运算。</p>

<blockquote><pre><code class="language-javascript">
// 以空格分割单词
var splitBySpace = s => s.split(' ');

// 每个单词的长度
var getLength = w => w.length;

// 词的数组转换成长度的数组
var getLengthArr = arr => R.map(getLength, arr); 

// 返回较大的数字
var getBiggerNumber = (a, b) => a > b ? a : b;

// 返回最大的一个数字
var findBiggestNumber = 
  arr => R.reduce(getBiggerNumber, 0, arr);
</code></pre></blockquote>

<p>然后，把基本运算合成为一个函数（查看<a href="http://jsbin.com/qusohax/edit?js,console">完整代码</a>）。</p>

<blockquote><pre><code class="language-javascript">
var getLongestWordLength = R.pipe(
  splitBySpace,
  getLengthArr,
  findBiggestNumber
);

getLongestWordLength(str) // 11
</code></pre></blockquote>

<p>可以看到，整个运算由三个步骤构成，每个步骤都有语义化的名称，非常的清晰。这就是 Pointfree 风格的优势。</p>

<p>Ramda 提供了很多现成的方法，可以直接使用这些方法，省得自己定义一些常用函数（查看<a href="http://jsbin.com/vutoxis/edit?js,console">完整代码</a>）。</p>

<blockquote><pre><code class="language-javascript">
// 上面代码的另一种写法
var getLongestWordLength = R.pipe(
  R.split(' '),
  R.map(R.length),
  R.reduce(R.max, 0)
);
</code></pre></blockquote>

<h2>六、Pointfree 示例二</h2>

<p>最后，看一个实战的例子，拷贝自 Scott Sauyet 的文章<a href="http://fr.umio.us/favoring-curry/">《Favoring Curry》</a>。那篇文章能帮助你深入理解柯里化，强烈推荐阅读。</p>

<p>下面是一段服务器返回的 JSON 数据。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031207.png" alt="" title="" /></p>

<p>现在要求是，找到用户 Scott 的所有未完成任务，并按到期日期升序排列。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031208.png" alt="" title="" /></p>

<p>过程式编程的代码如下（查看<a href="http://jsbin.com/kiqequ/edit?js,console">完整代码</a>）。</p>

<p><img src="http://www.ruanyifeng.com/blogimg/asset/2017/bg2017031209.png" alt="" title="" /></p>

<p>上面代码不易读，出错的可能性很大。</p>

<p>现在使用 Pointfree 风格改写（查看<a href="http://jsbin.com/xuhosef/edit?js,console">完整代码</a>）。</p>

<blockquote><pre><code class="language-javascript">
var getIncompleteTaskSummaries = function(membername) {
  return fetchData()
    .then(R.prop('tasks'))
    .then(R.filter(R.propEq('username', membername)))
    .then(R.reject(R.propEq('complete', true)))
    .then(R.map(R.pick(['id', 'dueDate', 'title', 'priority'])))
    .then(R.sortBy(R.prop('dueDate')));
};
</code></pre></blockquote>

<p>上面代码已经清晰很多了。</p>

<p>另一种写法是，把各个<code>then</code>里面的函数合成起来（查看<a href="http://jsbin.com/gexeme/edit?js,console">完整代码</a>）。</p>

<blockquote><pre><code class="language-javascript">
// 提取 tasks 属性
var SelectTasks = R.prop('tasks');

// 过滤出指定的用户
var filterMember = member => R.filter(
  R.propEq('username', member)
);

// 排除已经完成的任务
var excludeCompletedTasks = R.reject(R.propEq('complete', true));

// 选取指定属性
var selectFields = R.map(
  R.pick(['id', 'dueDate', 'title', 'priority'])
);

// 按照到期日期排序
var sortByDueDate = R.sortBy(R.prop('dueDate'));

// 合成函数
var getIncompleteTaskSummaries = function(membername) {
  return fetchData().then(
    R.pipe(
      SelectTasks,
      filterMember(membername),
      excludeCompletedTasks,
      selectFields,
      sortByDueDate,
    )
  );
};
</code></pre></blockquote>

<p>上面的代码跟过程式的写法一比较，孰优孰劣一目了然。</p>

<h2>七、参考链接</h2>

<ul>
<li><a href="http://lucasmreis.github.io/blog/pointfree-javascript/">Pointfree Javascript</a></li>
<li><a href="http://fr.umio.us/favoring-curry/">Favoring Curry</a></li>
</ul>

<p>（完）</p>

                                    <!-- /div -->

                                </div>
    <script type="text/javascript" src="/newwindow.js"></script>
                                <div class="asset-footer">

<h3>文档信息</h3>
<ul>
<li>版权声明：自由转载-非商用-非衍生-保持署名（<a href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh">创意共享3.0许可证</a>）</li>
<li>发表日期： <abbr class="published" title="2017-03-13T06:56:10+08:00">2017年3月13日</abbr></li>
<li>更多内容： <a href="http://www.ruanyifeng.com/blog/archives.html" target="_blank"> 档案</a>  » 
<a href="http://www.ruanyifeng.com/blog/javascript/"> JavaScript</a> 
</li>
<li>博客文集：<a href="http://road.ruanyifeng.com" target="_blank">《寻找思想之路》</a>，<a href="https://ruanyf.github.io/survivor" target="_blank">《未来世界的幸存者》</a></li>
<li>社交媒体：<a href="https://twitter.com/ruanyf" target="_blank"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAk1JREFUeNqsVc9rE0EU/mZ3dhPNJl2bVIk/Km09aFBE8GLvnrwJXvwLxIsgCP4Fnit6E8Gb0IMHwUsL9SSNgiAoooJIpE1Joo1h82uT7IxvxmRN3Q32kAdvdrI773vfe+/bDTu9WioDcDAda3Ja8piepQ1avCkCeny0Y+R9KenKwOmHHLvPaKn7AtVOoO8dOWDCMpg+41gMQv5FNEJACgoE8MsPNLDBhgfoutMOsJDmWLmU037C4TApciljwQ/kHoohQxV06+wMXNvE7WINuaSpvdYVKLgWnl3O4zAxU3Z1IYVGT+B5qYWV9z2kbQaT/cOwTsxOUUYF+mB5Dkmi8HG3h2q9hxsFNwRTdvQgxxnXRrMvIdkEhllis/qtiWuLDm4WZnBlPoWnXz28LHdw0uGR7m9Wu3j0qYGEubfn4UlBfXO4gTZltRNMg9w9f0i7kNFxllsBlS0x75gYfxyWTBUjT2W5CSMSPBrQuG21+hiMDS8CeCzF8eSLp13uQ3Ab1IqMFZN8tFHPmgOBF99bYP8Be1Xp6t7OJszJgKpPSiZvaj7uf2hguz2IBQuozDvFH6RDBjuK9wdQDvt0nMpW+8efGyh5UcAeZb2+UcHbnz5Jx4wdlp4yJYU3kLiQtfBwOYeLc8nIwfXtNu69q2Oz4mMxbemYOOOjKarhvq51KUjg3GwiFPIuvcNF6pnSnWK0lOEabNLgQh1aJFAhlGB9rG110B2+oyRNPc0sZbRNFltmLKDKqj4Qrm1ojzOxDz2pyPQ0P7CK4c40/wJ+CzAAGYrXsvfFXR4AAAAASUVORK5CYII=" style="border:0;"> twitter</a>，<a href="http://weibo.com/ruanyf" target="_blank"><img src="data:image/png;base64,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" style="border:0;" /> weibo</a></li>
<li>Feed订阅： <a href="/feed.html" target="_blank"><img src="data:image/gif;base64,R0lGODlhFAAUANU2APV1GfmrePZ8IeR5VPq2ieNkLf7p3NpFJveCJ/NoFfibVPR1IexiJfvdzuZrNfXGuOhUEueTevaFOfzIpNxDGeZZJNU6IOubifiVTfOnid1aLuZpLOFSJf/28vJtIvGcefaLSd5kNu9iFv/z6//48//t4uFfLfNkCeJNGuGNc/rCof/+/PVxEeldI/V5KeKMbu9nIvB2OvzQtNxMKfOPXP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAADYALAAAAAAUABQAAAb/QJstEjKZCsjCZsl0pIS2QWXaYsA8noVWIEAgFoNhhWNyMESi7Jbr/aZCFdRnZJAFJCwAt+vlOkwtEBk1hDUkExJ6bQJaGyYMLTQTDSOFHQF8jAseSFYiJwkuAQ2FE1xaHjBIMDAgARguJwABJIQTLJswDEgeIgSEJQQILAqVNQEiui1HHgkBhTUGCiwYtR0xLS0VJhtaEgoEBoQkGCfPNSoQY9xaCwAsCBPALgmkJA4cZN0CAAgY/PJqEIDwgVAECjM0bOAnwcAKGQJclKhRgoGDDjUeUDigkN8vQiBOfByAglSDAxw3IBCgYEU0FyJoEPpA4UGNDjMsaHDQR8EdPVYOMmQYQGHAhQgHLIRIsWAlgASsGMRBMWMGBQtYZ7yIsoBRKkhjOMxAiXJGGCEpHGxIYsSIhrcaQmy1EQQAOw==" style="border:0;" /></a></li>

</ul>
                                </div>
</article>
                            </div>

                        <div id="sup-post-2" style="display: inline-block ! important;width: 100%;">
   <p style="text-align:center;"><a href="http://www.zhufengpeixun.cn/jscourse/new/js/index.html?ref=ruanyifeng.com" target="_blank"><img alt="珠峰培训" src="http://www.ruanyifeng.com/blog/images/sup_zhufeng_page.png" style="border:none;"/></a></p>
   <p style="text-align:center;"><a href="https://cn.udacity.com/ruanyfbanner/" title="优达学城" target="_blank"><image alt="优达学城" src="https://s3.cn-north-1.amazonaws.com.cn/static-documents/marketing/uda_banner_ryf.jpg" style="border:none;display: block !important;" /></a>
</p>                         
  </div>

<div id="related_entries">
<h2>相关文章</h2>
<ul>

<li><strong>2017.03.18: <a href="http://www.ruanyifeng.com/blog/2017/03/reduce_transduce.html">Reduce 和 Transduce 的含义</a></strong>

                           <div class="entry-body">
                              学习函数式编程，必须掌握很多术语，否则根本看不懂文档。

                           </div>

</li>

 
<li><strong>2017.03.09: <a href="http://www.ruanyifeng.com/blog/2017/03/ramda.html">Ramda 函数库参考教程</a></strong>

                           <div class="entry-body">
                              学习函数式编程的过程中，我接触到了 Ramda.js。

                           </div>

</li>

 
<li><strong>2016.11.15: <a href="http://www.ruanyifeng.com/blog/2016/11/javascript.html">JavaScript 全栈工程师培训教程</a></strong>

                           <div class="entry-body">
                              我现在的技术方向，前端是 React，后端是 Node，时间都投入在这两方面。

                           </div>

</li>

 
<li><strong>2016.11.03: <a href="http://www.ruanyifeng.com/blog/2016/11/intersectionobserver_api.html">IntersectionObserver API 使用教程</a></strong>

                           <div class="entry-body">
                              网页开发时，常常需要了解某个元素是否进入了"视口"（viewport），即用户能不能看到它。

                           </div>

</li>

 
</ul>
</div>


<div id="gd1" style="display: block !important;">
<h2>广告<a href="/support.html">（购买广告位）</a></h2>
<div id="gd1-inner">
<div id="gd1-left">
<a href="http://www.miaov.com/?utm_source=ruanyifeng&" alt="妙味课堂" target="_blank"><image alt="妙味课堂" src="http://www.ruanyifeng.com/blog/images/sup_miaov_201703.jpg" style="border:none;display: block !important;" /></a>
<br />
<a href="http://www.zhinengshe.com/?utm_source=ruanyifeng&utm_medium=cpm&utm_campaign=extlink2016&utm_term=qianduan&utm_content=article" title="智能社" target="_blank"><image alt="智能社" src="http://www.ruanyifeng.com/blog/images/sup_zhinengshe.jpg" style="border:none;display: block !important;" /></a>
</div>
<div id="gd1-right">
<a href="http://apeclass.cn/1212/index.html?utm_source=ruanyifeng" title="海棠学院" target="_blank"><image alt="海棠学院" src="http://www.ruanyifeng.com/blog/images/sup_apeclass_300.png" style="border:none;display: block !important;" /></a>
<br />
<a href="http://www.ruanyifeng.com/support.html" target="_blank"><image src="http://www.ruanyifeng.com/blog/images/sup_sale_s.png" style="border:none;" /></a>

</div>
</div>
</div>
                    

                    <div id="comments" class="comments">


    
    
        
    <h2 class="comments-header">留言（29条）</h2>

    <div id="comments-content" class="comments-content" style="clear: left;">
        
        <div id="comment-374644" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">李冬杰</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374644">
            <p>解决了我的疑问，谢谢老师</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017  7:57 AM">2017年3月13日 07:57</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374644">#</a>
 | <a href="#comment-text" title="引用李冬杰的这条留言" onclick="return CommentQuote('comment-quote-374644','李冬杰');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374645" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">章鱼来</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374645">
            <p>每过一段时间回来翻翻阮老师的文章，收获巨大！</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017  9:04 AM">2017年3月13日 09:04</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374645">#</a>
 | <a href="#comment-text" title="引用章鱼来的这条留言" onclick="return CommentQuote('comment-quote-374645','章鱼来');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374648" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://szpzs.oschina.io/" href="http://szpzs.oschina.io/" target="_blank" rel="nofollow">szpzs</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374648">
            <p>谢谢阮老师，使得我更加理解函数式编程。</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017  9:33 AM">2017年3月13日 09:33</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374648">#</a>
 | <a href="#comment-text" title="引用szpzs的这条留言" onclick="return CommentQuote('comment-quote-374648','szpzs');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374649" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">czs</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374649">
            <p>柯里化确实使pointfree更加自然，感谢！</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017  9:35 AM">2017年3月13日 09:35</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374649">#</a>
 | <a href="#comment-text" title="引用czs的这条留言" onclick="return CommentQuote('comment-quote-374649','czs');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374651" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">任天缘</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374651">
            <p>有一种豁然开朗、拨云见日的感觉</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017  9:53 AM">2017年3月13日 09:53</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374651">#</a>
 | <a href="#comment-text" title="引用任天缘的这条留言" onclick="return CommentQuote('comment-quote-374651','任天缘');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374652" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://www.junqing.ren" href="http://www.junqing.ren" target="_blank" rel="nofollow">斑谷</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374652">
            <p>这个风格似乎不方便调试</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017 10:01 AM">2017年3月13日 10:01</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374652">#</a>
 | <a href="#comment-text" title="引用斑谷的这条留言" onclick="return CommentQuote('comment-quote-374652','斑谷');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374657" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">黄亮</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374657">
            <p>每每阅读阮老师的文章，感觉都收获巨大</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017 10:30 AM">2017年3月13日 10:30</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374657">#</a>
 | <a href="#comment-text" title="引用黄亮的这条留言" onclick="return CommentQuote('comment-quote-374657','黄亮');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374658" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">RedNax</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374658">
            <p>并没有觉得这个解释了“函数式编程有什么用”，只是解答了“函数式编程怎么用”……</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017 10:41 AM">2017年3月13日 10:41</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374658">#</a>
 | <a href="#comment-text" title="引用RedNax的这条留言" onclick="return CommentQuote('comment-quote-374658','RedNax');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374659" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://www.xttblog.com" href="http://www.xttblog.com" target="_blank" rel="nofollow">业余草</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374659">
            <p>函数式编程是一种编程的模式，在这种编程模式中最常用的函数和表达式。它强调在编程的时候用函数的方式思考问题，函数也与其他数据类型一样，处于平等地位。可以将函数作为参数传入另一个函数，也可以作为别的函数的返回值。函数式编程倾向于用一系列嵌套的函数来描述运算过程。</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017 10:49 AM">2017年3月13日 10:49</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374659">#</a>
 | <a href="#comment-text" title="引用业余草的这条留言" onclick="return CommentQuote('comment-quote-374659','业余草');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374661" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">cologler</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374661">
            <p>最后的例子是强行加长了过程式编程的代码的吧？<br />
一个 then 就完了非要写成五个。</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017 11:05 AM">2017年3月13日 11:05</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374661">#</a>
 | <a href="#comment-text" title="引用cologler的这条留言" onclick="return CommentQuote('comment-quote-374661','cologler');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374663" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://yingbo.miao.fm" href="http://yingbo.miao.fm" target="_blank" rel="nofollow">yingbo</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374663">
            <p>Pointfree风格的getIncompleteTaskSummaries看起来很美，可是如果数据格式有可能错误就很麻烦；而且调试也很麻烦。</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017 11:59 AM">2017年3月13日 11:59</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374663">#</a>
 | <a href="#comment-text" title="引用yingbo的这条留言" onclick="return CommentQuote('comment-quote-374663','yingbo');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374670" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">小烈</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374670">
            <p>Algebra of Programming对point-free programming有深入的阐发</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 13, 2017  3:01 PM">2017年3月13日 15:01</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374670">#</a>
 | <a href="#comment-text" title="引用小烈的这条留言" onclick="return CommentQuote('comment-quote-374670','小烈');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374690" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">alvin2ye</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374690">
            <blockquote>
<pre>引用斑谷的发言：</pre>

<p>这个风格似乎不方便调试</p>

</blockquote>

<p>恰恰相反, 函数式编程最大的好处之一就是方便调试. </p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 14, 2017  9:23 AM">2017年3月14日 09:23</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374690">#</a>
 | <a href="#comment-text" title="引用alvin2ye的这条留言" onclick="return CommentQuote('comment-quote-374690','alvin2ye');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374693" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://www.xuechenlei.com" href="http://www.xuechenlei.com" target="_blank" rel="nofollow">jone</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374693">
            <p>奔腾的编码思想根本停不下来，预感人工智能最终要占领地球</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 14, 2017 10:19 AM">2017年3月14日 10:19</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374693">#</a>
 | <a href="#comment-text" title="引用jone的这条留言" onclick="return CommentQuote('comment-quote-374693','jone');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374694" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://www.xuechenlei.com" href="http://www.xuechenlei.com" target="_blank" rel="nofollow">jone</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374694">
            <p>回头再把柯里化的内容再看下</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 14, 2017 10:26 AM">2017年3月14日 10:26</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374694">#</a>
 | <a href="#comment-text" title="引用jone的这条留言" onclick="return CommentQuote('comment-quote-374694','jone');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374790" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">zhlsky</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374790">
            <p>阮老师<br />
你好。<br />
您的这篇文章对我启发很大。<br />
我个人有些疑问。<br />
我对于pointfree的理解是：<br />
1. 借助于柯里化把多参函数改写成单参函数<br />
2. 在pipeline里，由于隐式的参数传递, 可以对子函数进行无参调用<br />
这样一来就和参数无关了，切合了pointfree这个观点。</p>

<p>在<br />
// 返回较大的数字<br />
var getBiggerNumber = (a, b) => a > b ? a : b;<br />
这里是双参。可以删除这个函数而将<br />
var findBiggestNumber = <br />
  arr => R.reduce(getBiggerNumber, 0, arr);<br />
改为<br />
var findBiggestNumber = <br />
  arr => Math.max(...arr)<br />
这样会不会好一些呢？</p>

<p>filterMember(member name),<br />
这个调用可不可以改成无参调用呢？</p>

<p>我参考的是下面这个链接：<br />
<a href="http://xahlee.info/comp/point-free_programing.html" rel="nofollow">http://xahlee.info/comp/point-free_programing.html</a></p>

<p>再次谢谢你的博文。<br />
</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 15, 2017  1:04 PM">2017年3月15日 13:04</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374790">#</a>
 | <a href="#comment-text" title="引用zhlsky的这条留言" onclick="return CommentQuote('comment-quote-374790','zhlsky');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374948" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">Jlc</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374948">
            <p>谢谢您的博文，谢谢您的知识分享。</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 17, 2017 11:34 AM">2017年3月17日 11:34</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374948">#</a>
 | <a href="#comment-text" title="引用Jlc的这条留言" onclick="return CommentQuote('comment-quote-374948','Jlc');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374984" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">小菜鸟</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374984">
            <p>讲的很详细，很容易理解，谢谢！</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 17, 2017  8:48 PM">2017年3月17日 20:48</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374984">#</a>
 | <a href="#comment-text" title="引用小菜鸟的这条留言" onclick="return CommentQuote('comment-quote-374984','小菜鸟');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-374986" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">cshenger</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-374986">
            <p>世界上没有什么问题是一个函数不能解决的，如果有就两个，如果还有就多个^_^</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 17, 2017 10:46 PM">2017年3月17日 22:46</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-374986">#</a>
 | <a href="#comment-text" title="引用cshenger的这条留言" onclick="return CommentQuote('comment-quote-374986','cshenger');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375008" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://catbaron.com/blog" href="http://catbaron.com/blog" target="_blank" rel="nofollow">catbaron</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375008">
            <p>这篇还是在说「怎么用」，而不是在说「为什么要用」。<br />
最后用于比对的代码也带有强烈的目的性，过程式的代码是把函数定义放到过程中，函数式代码确是引用已经定义的函数，当然后者会易读一些。</p>

<p>所以我们到底为什么需要纯函数的编程？</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 18, 2017 10:26 AM">2017年3月18日 10:26</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375008">#</a>
 | <a href="#comment-text" title="引用catbaron的这条留言" onclick="return CommentQuote('comment-quote-375008','catbaron');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375055" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="http://无" href="http://无" target="_blank" rel="nofollow">Reese Laye</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375055">
            <p>我一直以来都只用OOP，是函数式编程的小白。此文及<a href='http://www.ruanyifeng.com/blog/2017/02/fp-tutorial.html' rel="nofollow">《函数式编程入门教程》</a>对我帮助很大，因为我开始了解到函数式编程的巨大优势！</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 18, 2017  6:45 PM">2017年3月18日 18:45</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375055">#</a>
 | <a href="#comment-text" title="引用Reese Laye的这条留言" onclick="return CommentQuote('comment-quote-375055','Reese Laye');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375078" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">changsj</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375078">
            <p>最后的例子非常直观，直观得就像SQL</p>

<p>越写越像 SQL ，这些查找数据的操作 <br />
越写越像 SQL ，这些处理数据的操作</p>

<p>搞数据库 用SQL语言，那是不需要for循环的 ---- 真的和函数式编程好像。我喜欢 </p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 19, 2017  5:46 PM">2017年3月19日 17:46</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375078">#</a>
 | <a href="#comment-text" title="引用changsj的这条留言" onclick="return CommentQuote('comment-quote-375078','changsj');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375079" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">juming </span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375079">
            <blockquote>
<pre>引用业余草的发言：</pre>

<p>函数式编程是一种编程的模式，在这种编程模式中最常用的函数和表达式。它强调在编程的时候用函数的方式思考问题，函数也与其他数据类型一样，处于平等地位。可以将函数作为参数传入另一个函数，也可以作为别的函数的返回值。函数式编程倾向于用一系列嵌套的函数来描述运算过程。</p>

</blockquote>

<p>这句话说得中肯。</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 19, 2017  7:11 PM">2017年3月19日 19:11</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375079">#</a>
 | <a href="#comment-text" title="引用juming 的这条留言" onclick="return CommentQuote('comment-quote-375079','juming ');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375291" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">knightlyj</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375291">
            <p>我感觉例子跟面向对象或者过程差不多,只是把函数拆分得更细,方便测试,不容易出错.</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 22, 2017  9:11 PM">2017年3月22日 21:11</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375291">#</a>
 | <a href="#comment-text" title="引用knightlyj的这条留言" onclick="return CommentQuote('comment-quote-375291','knightlyj');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375347" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">zxldev</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375347">
            <p> R.pipe(<br />
      SelectTasks,//第一数据入口<br />
      filterMember(membername),<br />
      excludeTasks(<br />
                              R.pipe(<br />
                                    SelectTasks,//第二数据入口<br />
                                    filterMember(membername),<br />
                                    excludeTasks('Completed'),<br />
                                    selectFields,<br />
                                    sortByDueDate,<br />
                            )<br />
      ),<br />
      selectFields,<br />
      sortByDueDate,<br />
      switchType(<br />
                         R.pipe(//第一分支出口<br />
                                    SelectTasks,<br />
                                    ……<br />
                            ), <br />
                         R.pipe(//第二分支出口<br />
                                    SelectTasks,<br />
                                   ……<br />
                            ), <br />
                         R.pipe(//第三分支出口<br />
                                    SelectTasks,<br />
                                   ……<br />
                            )<br />
                         ),<br />
    )</p>

<p>- -！</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 23, 2017  4:16 PM">2017年3月23日 16:16</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375347">#</a>
 | <a href="#comment-text" title="引用zxldev的这条留言" onclick="return CommentQuote('comment-quote-375347','zxldev');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375449" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author"><a title="https://daochuchao.github.io/" href="https://daochuchao.github.io/" target="_blank" rel="nofollow">到处抄</a></span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375449">
            <p>并没有觉得这个解释了“函数式编程有什么用”，只是解答了“函数式编程怎么用”……</p>

<p>应该理解到本文说函数式编程提供了一种思考问题的方式，这种方式就是pointfree,通过函数的嵌套避免了循环等东西</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 25, 2017 11:52 PM">2017年3月25日 23:52</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375449">#</a>
 | <a href="#comment-text" title="引用到处抄的这条留言" onclick="return CommentQuote('comment-quote-375449','到处抄');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-375611" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">u9</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-375611">
            <p>data.tasks.filter(i=>i.username=='Scott').sort((p,q)=>p.dueDate>q.dueDate)<br />
还是喜欢酱紫</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="March 29, 2017 10:14 AM">2017年3月29日 10:14</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-375611">#</a>
 | <a href="#comment-text" title="引用u9的这条留言" onclick="return CommentQuote('comment-quote-375611','u9');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-376054" class="comment">
    <div  class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">YuanChieh</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-376054">
            <p>十分精闢的博文！看完十分想要將函數式編程套用在日常開發中。<br />
但我想請教老師，假設我現在是以開發網站後台的角度，我勢必會有 非Point-free的操作(DB/ IO等)與可以套用函數式編程的純資料運算的地方，請教老師能否以開發網站後台角度分享 如何將原本的過程式編程融合函數式編程開發呢？<br />
目前對於這部分感到有些許混淆，再次感謝老師的分享</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="April  8, 2017  3:48 PM">2017年4月 8日 15:48</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-376054">#</a>
 | <a href="#comment-text" title="引用YuanChieh的这条留言" onclick="return CommentQuote('comment-quote-376054','YuanChieh');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    
        
        <div id="comment-376133" class="comment">
    <div id="comment-last" class="inner">
        <div class="comment-header">
            <div class="asset-meta">
<p>
                <span class="byline">
                    

                    <span class="vcard author">cc</span>

 说：
                </span>
</p>
            </div>
        </div>
        <div class="comment-content" id="comment-quote-376133">
            <p>这个用lisp搞起来是不是更简单？</p>
        </div>
<div class="comment-footer">
<div class="comment-footer-inner">
<p>
                   <abbr class="published" title="April 10, 2017  6:40 PM">2017年4月10日 18:40</abbr>
 | <a href="http://www.ruanyifeng.com/blog/2017/03/pointfree.html#comment-376133">#</a>
 | <a href="#comment-text" title="引用cc的这条留言" onclick="return CommentQuote('comment-quote-376133','cc');">引用</a>
</p>
</div>
</div>
    </div>
</div>
        
    </div>
        
    


    
    
    <div class="comments-open" id="comments-open">
        <h2 class="comments-open-header">我要发表看法</h2>
        <div class="comments-open-content">

        
            <div id="comment-greeting"></div>

            <form method="post" action="http://www.ruanyifeng.com/cgi-bin/mtos/mt-comments.cgi" name="comments_form" id="comments-form" onsubmit="return pleaseWait();">
                <input type="hidden" name="static" value="1" />
                <input type="hidden" name="entry_id" value="1925" />
                <input type="hidden" name="__lang" value="en" />
                <input type="hidden" name="parent_id" value="" id="comment-parent-id" />
                <input type="hidden" name="armor" value="1" />
                <input type="hidden" name="preview" value="" />
                <input type="hidden" name="sid" value="" />
                <div id="comments-open-data">
            <div id="comments-open-text">
                    <p><label for="comment-text">您的留言
                    （HTML标签部分可用）</label></p>
                    <p><textarea id="comment-text" name="text" rows="10" cols="50"></textarea></p>
                </div>
                    <div id="comment-form-name">
                        <p><label for="comment-author">您的大名：</label></p>
                        <p><input id="comment-author" name="author" size="30" value="" />  <span class="hint"> &laquo;-必填</span></p>
                    </div>
                    <div id="comment-form-email">
                        <p><label for="comment-email">电子邮件：</label></p>
                        <p><input id="comment-email" name="email" size="30" value="" />  <span class="hint"> &laquo;-必填，不公开</span></p>
                    </div>
                    <div id="comment-form-url">
                        <p><label for="comment-url">个人网址：</label></p>
                        <p><input id="comment-url" name="url" size="30" value="" />  <span class="hint"> &laquo;-我信任你，不会填写广告链接</span></p>
                    </div>
                    <div id="comment-form-remember-me">
                        <p>
                        <label for="comment-bake-cookie">记住个人信息？</label><input type="checkbox" id="comment-bake-cookie" name="bakecookie" onclick="!this.checked?forgetMe(document.comments_form):rememberMe(document.comments_form)" value="1" accesskey="r" /></p>
                    </div>
                </div>
                    <div id="comment-form-reply" style="display:none">
                    <input type="checkbox" id="comment-reply" name="comment_reply" value="" onclick="mtSetCommentParentID()" />
                    <label for="comment-reply" id="comment-reply-label"></label>
                </div>
                <div id="comments-open-captcha"></div>
                <div id="comments-open-footer">
<div id="wait" style="display:none;">
<p><strong>正在发表您的评论，请稍候</strong></p>
<p>
<input type="text" name="percent" size="3" style="font-family:Arial; color:black;text-align:center; border-width:medium; border-style:none;">           
<input type="text" name="chart" size="46" style="font-family:Arial;font-weight:bolder; color:black; padding:0px; border-style:none;">
</p>
</div>

                    <p><input type="submit" accesskey="s" name="post" id="comment-submit" value="发表" />  <span class="hint"> &laquo;- 点击按钮</span></p>
                </div>
            </form>


        </div>
    </div>

    


</div>




                        </div>
                    </div>

                </div>
            </div>
        <script type="text/javascript" src="http://www.ruanyifeng.com/blog/js/prism.js"></script>

            <div id="footer">
    <div id="footer-inner">
        <div id="footer-content">
<p><a href="/contact.html">联系方式</a> | ruanyifeng.com 2003 - 2017

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-46829782-1', 'ruanyifeng.com');
  ga('send', 'pageview');

</script>



<!-- Site Meter -->
<a href="http://sm3.sitemeter.com/stats.asp?site=sm3bomoocom" target="_top">
<img src="http://sm3.sitemeter.com/meter.asp?site=sm3bomoocom" alt="Site Meter" border="0"/></a>

<!-- Copyright (c)2009 Site Meter -->

</p>

        </div>
    </div>
</div>


<div id="share_button_proto" style="display:none;">
<a class="bshareDiv" href="http://www.bshare.cn/share">分享按钮</a>



<script type="text/javascript" charset="utf-8" src="http://static.bshare.cn/b/buttonLite.js#uuid=15e016b4-0028-44f1-a40d-a3c9d9c13c28&style=10&bgcolor=#fff&bp=facebook,twitter,sinaminiblog,weixin,gplus,qqmb,qzone,douban,qqim,fanfou,instapaper,xueqiu&ssc=false"></script>
<script type="text/javascript" charset="utf-8">
bShare.addEntry({
    title: document.getElementById("page-title").innerHTML,
url:window.location.href
});
</script>
</div>

<script>
document.getElementById("share_button").innerHTML=document.getElementById("share_button_proto").innerHTML;
</script>




        </div>
    </div>
</body>
</html>''')
