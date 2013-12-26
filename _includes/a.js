<script type="text/javascript">
var z = 8,
    w = $('header').width() - ($('header').width() % z) || 960,
    h = (window.innerHeight - $('header').outerHeight(true) - $('footer').outerHeight(true)) - (window.innerHeight % z) || 600,
    x = w / z,
    y = h / z;

d3.select("#art").insert("svg:svg")
  .attr("width", w)
  .attr("height", h);

d3.select("svg").selectAll("rect")
    .data(d3.range(x * y))
  .enter().append("svg:rect")
    .attr("transform", translate)
    .attr("width", z)
    .attr("height", z)
    .style("fill","#709070")
    .style("fill-opacity",0);

function translate(d) {
  return "translate(" + (d % x) * z + "," + Math.floor(d / x) * z + ")";
}

function m_dist(target, d) {
    var dx = d % x;
    var dy = Math.floor(d / x);
    var tx = target % x;
    var ty = Math.floor(target / x);

    return Math.abs(dx - tx) + Math.abs(dy - ty);
}

function r_dist (t, d) {
    var dx = d % x;
    var dy = Math.floor(d / x);
    var tx = t % x;
    var ty = Math.floor(t / x);

    return Math.max(Math.abs(dx - tx), Math.abs(dy - ty));
}

function pickNode() {
  var rnd = Math.round(Math.random() * x * y);

  d3.selectAll("rect")
    .filter(function(d) {
        var is_part = false;
        var r = 0;
        for (var i = r; i >= (0-r); i--) {
            var b = rnd - i*x;
            is_part = is_part || Math.abs(d - b) <= r;
        };
        return is_part;
    })
    .each(function(d) {
        var l = Math.round(Math.random() * 1000) + 1500;
        var decay = 0.5 - (m_dist(rnd, d) * 0.2);

        d3.select(this).transition()
          // .duration(function () { return Math.round(Math.random() * 1000) + 1500; })
          .duration(l)
          .style("fill-opacity", 0.8)
        .transition()
          .delay(2500)
          .duration(l)
          .style("fill-opacity", 0);
    });
}

var toggle_animation = (function () {
    var state = 0;
    var s2 = 0;
    return function () {
        if (state) {
            window.clearInterval(state);
            state = 0;

            if (w * h > 272000) {
                window.clearInterval(s2);
                s2 = 0;
            }
        } else {
            state = window.setInterval(pickNode, 500);
            if (w * h > 272000) {
                s2 = window.setInterval(pickNode, 500);
            }
        }
    }
})();

$('#main').click(function() {
    toggle_animation();
    event.preventDefault();
});

toggle_animation();
</script>
