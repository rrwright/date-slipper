<html>
	<body class="c19">
		<h1 class="c9 title">
			<a name="h.9b7fvp1mtspm"></a><span>Date Slipper v1.0</span>
		</h1>
		<h1 class="c9"><a name="h.kudk4w2qhnm6"></a><span>The Problem This Solves</span></h1>
		<p class="c9">
			<span>Predicting delivery dates is hard! The further out an estimate is, the less precise we can be about the time period in which it is delivered. Errors compound and the longer a project takes, the more delays affect it. If the project will take 1 hour, we might accurately estimate delivery within a handful of minutes. But if delivery will take 5 months, we cannot estimate to within the same handful of minutes. The solution is to decrease the precision of the estimated timeframe the later you go. But this is much harder than it looks&hellip;</span>
		</p><h1 class="c9"><a name="h.bvsjw9w6rwtb"></a><span>Why This Is Difficult</span></h1>
		<p class="c9">
			<span>As with most problems, setting up the problem in the right way is 80% of the solution. This is a hard problem to think about until you have the right framework in which assemble a solution. While putting that framework together, you have to know to consider&mdash;and be able to address&mdash;at least the following concerns:</span>
		</p>
		<ol class="c18" start="1">
			<li class="c11 c9">
				<span>Loss of precision over time: the longer the timeframe, the less precise the estimate.</span>
			</li>
			<li class="c11 c9">
				<span>Delivery needs to be broken in to discrete timeframes instead of simply &plusmn; some range&mdash;otherwise the audience naturally computes the middle of the range as a real date.</span>
			</li>
			<li class="c11 c9">
				<span>Projects are very rarely early. Lack of accuracy from an estimate almost always means the delivery will be later, not earlier.</span>
			</li>
			<li class="c11 c9">
				<span>Delivering early is possible and should probably happen more often.</span>
			</li>
			<li class="c11 c9">
				<span>Delivery estimates need to get increasingly more accurate as time goes on so that what was once a far-off estimate with low precision will eventually be a near estimate with high precision. That transition needs to happen smoothly and naturally.</span>
			</li>
			<li class="c11 c9">
				<span>If a delivery is projected to occur near the end of a certain time frame, it is better to estimate that it be delivered in the next time frame. For example, calculated delivery on June 30th should be estimated as Q3, not Q2.</span>
			</li>
		</ol><h2 class="c9"><a name="h.ibvooma2zayj"></a><span>This does not solve&hellip;</span></h2>
		<ol class="c18" start="1">
			<li class="c11 c9">
				<span>Deriving the original estimate.</span>
			</li>
			<li class="c11 c9">
				<span>Delivering your product.</span>
			</li>
		</ol>
		<p class="c1">
			<span></span>
		</p>
		<p class="c1">
			<span></span>
		</p><h1 class="c9"><a name="h.inzyepa6f2e2"></a><span>Our Solution</span></h1><h2 class="c9"><a name="h.xt7eb0kvspwt"></a><span>Discrete problems:</span></h2>
		<ol class="c16" start="1">
			<li class="c11 c9">
				<span>Create &ldquo;stepped&rdquo; timeframes</span>
			</li>
			<li class="c9 c11">
				<span>Determine which timeframe to use for any particular estimate</span>
			</li>
		</ol><h2 class="c9"><a name="h.pubtvvm4h8ma"></a><span>Create Stepped Timeframes:</span></h2>
		<p class="c9">
			<span>The final output we want to display is a textual explanation of the timeframe expected for delivery. Examples of this include &ldquo;late August&rdquo; or &ldquo;mid Q1&rdquo; or even &ldquo;March 19&rdquo;. To accomplish this, we set up arrays of the possible components of each textual timeframe to be combined in various ways:</span>
		</p>
		<p class="c15 c9">
			<span class="c6">portions = [&quot;early &quot;, &quot;mid &quot;, &quot;late &quot;]</span>
		</p>
		<p class="c9 c15">
			<span class="c6">months = [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;, &quot;Apr&quot;, &quot;May&quot;, &quot;Jun&quot;, &quot;Jul&quot;, &quot;Aug&quot;, &quot;Sep&quot;, &quot;Oct&quot;, &quot;Nov&quot;, &quot;Dec&quot;]</span>
		</p>
		<p class="c15 c9">
			<span class="c6">quarters = [&quot;Q1&quot;, &quot;Q2&quot;, &quot;Q3&quot;, &quot;Q4&quot;]</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>These components can be combined (with numerals) to represent all of the following types of timeframes:</span>
		</p>
		<p class="c9">
			<span>Day: </span><span class="c6">Mar 19</span>
		</p>
		<p class="c9">
			<span>Partial-Month: </span><span class="c6">early Jan</span>
		</p>
		<p class="c9">
			<span>Partial-Quarter (or Month): </span><span class="c6">late Q2</span>
		</p>
		<p class="c9">
			<span>Quarter: </span><span class="c6">Q3 2014</span>
		</p>
		<p class="c9">
			<span>Year: </span><span class="c6">2015</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>We can think of these categories as an array of precision:</span>
		</p>
		<p class="c9">
			<span class="c6">precision = [ Day, Partial-Month, Partial-Quarter, Quarter, Year ]</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>Each of these timeframes corresponds with a level of precision we want to use for estimating delivery. The daily timeframes suggests a level of precision within one day. The partial month timeframes suggests a level of precision to within approximately 1/3 of a month (or a little more than a week). Etcetera.</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>With the arrays described above (portions, months, and quarters) and numeric representation of days and years, we can assemble any combination of the timeframes described above. The next step is to calculate the proper assemblage.</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>Consider the following list of numbers:</span>
		</p>
		<p class="c9">
			<span class="c6">0, 10, 21, 37, 59, 91, 137, 200, 283, 388</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>The important feature for our purposes is the distance between these numbers; that is to say, if you take any number and subtract the number before it, these numbers fall into &nbsp;groups related to the timeframes we want to generate.</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>The first number (0) is a special case. There is nothing before it, and this number alone corresponds with the daily timeframe. Since the daily timeframe is the most exact timeframe possible, there is only one possible category for this timeframe: exact.</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>The next three numbers (10, 21, 37), when subtracting the number before it, return: 10, 11, 16 (these are the intervals between the numbers). These interval values&mdash;as numbers of days&mdash;correspond approximately with the number of days in each partial-month timeframe (~10).</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>The next three numbers (59, 91, 137) have intervals of: 22, 32, 46. These intervals correspond approximately with the number of days in each monthly or partial-quarter timeframe (~31).</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>The next three numbers (200, 283, 388) have intervals of: 63, 83, 105. These intervals correspond approximately with the number of days in each quarterly timeframe (~90).</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>Anything higher than those intervals corresponds with the yearly intervals, although after three yearly intervals, we skip to a final category and just admit that the timeframe is &ldquo;probably never&rdquo;.</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>This series of numbers is generated by plugging successive integer values of </span><span class="c0">x</span><span>&nbsp;into the following equation:</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c5">
			<span class="c0">y</span><span>&nbsp;= 11</span><span class="c0">x</span><span>&nbsp;- 1.2</span><span class="c0">x</span><span class="c8">2</span><span>&nbsp;+ 0.53</span><span class="c0">x</span><span class="c8">3</span>
		</p>
		<p class="c1">
			<span></span>
		</p><a href="#" name="ace5e76c36727ddfb68387011e9db620069376bd"></a><a href="#" name="0"></a>
		<table cellpadding="0" cellspacing="0" class="c17">
			<tbody>
				<tr>
					<td class="c14">
					<p class="c3">
						<span>x = 1</span>
					</p></td><td class="c10">
					<p class="c3">
						<span>y = 0</span>
					</p></td>
				</tr>
				<tr>
					<td class="c14">
					<p class="c3">
						<span>x = 2</span>
					</p></td><td class="c10">
					<p class="c3">
						<span>y = 10</span>
					</p></td>
				</tr>
				<tr>
					<td class="c14">
					<p class="c3">
						<span>x = 3</span>
					</p></td><td class="c10">
					<p class="c3">
						<span>y = 21</span>
					</p></td>
				</tr>
				<tr>
					<td class="c14">
					<p class="c3">
						<span>x = 4</span>
					</p></td><td class="c10">
					<p class="c3">
						<span>y = 37</span>
					</p></td>
				</tr>
				<tr>
					<td class="c14">
					<p class="c3">
						<span>x = 5</span>
					</p></td><td class="c10">
					<p class="c3">
						<span>y = 59</span>
					</p></td>
				</tr>
				<tr>
					<td class="c14">
					<p class="c3">
						<span>&hellip;</span>
					</p></td><td class="c10">
					<p class="c3">
						<span>&hellip;</span>
					</p></td>
				</tr>
			</tbody>
		</table>
		<p class="c1">
			<span></span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>The result is the array of numbers listed above. The index of each item in this array is of special use to us in solving our stepped timeframe problem. The index of each number divided by 3 and rounded up (&ldquo;ceiling&rdquo;) is the index into the needed precision. (Note: a partial differential could also be used.)</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c1">
			<span></span>
		</p><a href="#" name="a6242d697c26d2ba1e267cc46df9d1268f8002ba"></a><a href="#" name="1"></a>
		<table cellpadding="0" cellspacing="0" class="c17">
			<tbody>
				<tr>
					<td class="c2">
					<p class="c3">
						<span class="c12">x =</span>
					</p></td><td class="c2">
					<p class="c3">
						<span class="c12">y =</span>
					</p></td><td class="c2">
					<p class="c3">
						<span class="c12">precision</span>
					</p></td>
				</tr>
				<tr>
					<td class="c2">
					<p class="c3">
						<span>0</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>0</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>daily</span>
					</p></td>
				</tr>
				<tr>
					<td class="c2">
					<p class="c3">
						<span>1, 2, 3</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>1</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>partial-month</span>
					</p></td>
				</tr>
				<tr>
					<td class="c2">
					<p class="c3">
						<span>4, 5, 6</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>2</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>partial-quarter</span>
					</p></td>
				</tr>
				<tr>
					<td class="c2">
					<p class="c3">
						<span>7, 8, 9</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>3</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>quarter</span>
					</p></td>
				</tr>
				<tr>
					<td class="c2">
					<p class="c3">
						<span>10, 11, 12</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>4</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>year</span>
					</p></td>
				</tr>
				<tr>
					<td class="c2">
					<p class="c3">
						<span>&gt; 12</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>5</span>
					</p></td><td class="c2">
					<p class="c3">
						<span>never</span>
					</p></td>
				</tr>
			</tbody>
		</table>
		<p class="c1">
			<span></span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>Now we have what we need to create an array of timeframes. Our implementations take a functional approach, so we wait to create the actual text until the delivery estimate is ready&hellip; which is the next step.</span>
		</p><h2 class="c9"><a name="h.m8dczt3ujv77"></a><span>Determine Which Timeframe To Use:</span></h2>
		<p class="c9">
			<span>Choosing the proper timeframe is also more difficult than it seems at first. The challenge lies primarily in smoothly slipping to the following timeframe when a delivery estimate falls near the very end of one particular timeframe. We accomplish this with a second function which runs near to the initial curve, but will slip to the next timeframe as the delivery estimate approaches the end of a timeframe.</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c5">
			<span class="c0">y</span><span>&nbsp;= 13</span><span class="c0">x</span><span class="c8">0.113</span><span>&nbsp;- 16.5</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>In this equation, </span><span class="c0">x</span><span>&nbsp;is the delivery estimate, and when rounded up to either 0 (&ldquo;max&rdquo;) or the next whole number (&ldquo;ceiling&rdquo;), </span><span class="c0">y</span><span>&nbsp;is an index into our &ldquo;intervals&rdquo; array. The result is another time in days close to the delivery estimate. </span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>We can take the larger of the two numbers as the appropriate timeframe to use for the final estimate. The number that is used is the original delivery estimate in most cases, unless that would fall near the end of a calculated timeframe. If it is near the end, the larger value returned from &ldquo;intervals&rdquo; is used and the final result is the next timeframe.</span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>For example:</span>
		</p>
		<p class="c1">
			<span></span>
		</p><a href="#" name="85a0a758a5bd2363642db523530da4ff019f7dd3"></a><a href="#" name="2"></a>
		<table cellpadding="0" cellspacing="0" class="c17">
			<tbody>
				<tr>
					<td class="c7">
					<p class="c3">
						<span class="c12">delivery</span>
					</p></td><td class="c10">
					<p class="c3">
						<span class="c12">y</span>
					</p></td><td class="c13">
					<p class="c3">
						<span class="c12">intervals(y)</span>
					</p></td><td class="c7">
					<p class="c3">
						<span class="c12">precision</span>
					</p></td><td class="c7">
					<p class="c3">
						<span class="c12">final result</span>
					</p></td>
				</tr>
				<tr>
					<td class="c7">
					<p class="c4">
						<span>5</span>
					</p></td><td class="c10">
					<p class="c4">
						<span>-0.907</span>
					</p></td><td class="c13">
					<p class="c4">
						<span>0 days</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>daily</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>Feb 22</span>
					</p></td>
				</tr>
				<tr>
					<td class="c7">
					<p class="c4">
						<span>20</span>
					</p></td><td class="c10">
					<p class="c4">
						<span>1.737</span>
					</p></td><td class="c13">
					<p class="c4">
						<span>21 days</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>partial-month</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>early Mar</span>
					</p></td>
				</tr>
				<tr>
					<td class="c7">
					<p class="c4">
						<span>70</span>
					</p></td><td class="c10">
					<p class="c4">
						<span>4.511</span>
					</p></td><td class="c13">
					<p class="c4">
						<span>91 days</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>partial-quarter</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>mid Q2</span>
					</p></td>
				</tr>
				<tr>
					<td class="c7">
					<p class="c4">
						<span>160</span>
					</p></td><td class="c10">
					<p class="c4">
						<span>6.568</span>
					</p></td><td class="c13">
					<p class="c4">
						<span>200 days</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>quarter</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>Q3 2013</span>
					</p></td>
				</tr>
				<tr>
					<td class="c7">
					<p class="c4">
						<span>700</span>
					</p></td><td class="c10">
					<p class="c4">
						<span>10.75</span>
					</p></td><td class="c13">
					<p class="c4">
						<span>681 days</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>yearly</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>2015</span>
					</p></td>
				</tr>
				<tr>
					<td class="c7">
					<p class="c4">
						<span>1200</span>
					</p></td><td class="c10">
					<p class="c4">
						<span>12.47</span>
					</p></td><td class="c13">
					<p class="c4">
						<span>1105 days</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>never</span>
					</p></td><td class="c7">
					<p class="c4">
						<span>probably never</span>
					</p></td>
				</tr>
			</tbody>
		</table>
		<p class="c1">
			<span></span>
		</p>
		<p class="c1">
			<span></span>
		</p>
		<p class="c9">
			<span>The end result is a timeframe using a graduated precision which has the expected delivery date comfortably within that timeframe.</span>
		</p>
	</body>
</html>